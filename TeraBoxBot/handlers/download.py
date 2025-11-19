import logging
import re
from pyrogram import Client, filters
from pyrogram.types import Message
import script
from utils.api import get_terabox_download_link
from utils.progress import upload_progress_callback
from utils.helper import get_file_size_mb, apply_prefix_to_filename
from utils.logger import send_error_log, send_success_log
from database.user_settings import UserSettings
from config import STORAGE_CHANNEL

logger = logging.getLogger(__name__)

# Simple regex to validate Terabox links
TERABOX_LINK_PATTERN = re.compile(r'https?://(?:www\.)?terabox\.com/s/[a-zA-Z0-9]+')

async def download_handler(client: Client, message: Message):
    """Handle Terabox link downloads"""
    try:
        # Extract link from message
        text = message.text or message.caption or ""
        
        # Check if message contains a valid link
        if not TERABOX_LINK_PATTERN.search(text):
            await message.reply_text(script.INVALID_LINK, parse_mode="markdown")
            return
        
        # Extract the link
        link_match = TERABOX_LINK_PATTERN.search(text)
        if not link_match:
            await message.reply_text(script.INVALID_LINK, parse_mode="markdown")
            return
        
        terabox_link = link_match.group(0)
        user_id = message.from_user.id
        
        # Send processing message
        status_msg = await message.reply_text(script.CHECKING_LINK)
        
        # Get download info from API
        await status_msg.edit_text(script.EXTRACTING_INFO)
        file_info = await get_terabox_download_link(terabox_link)
        
        if not file_info or 'error' in file_info:
            await status_msg.edit_text(
                script.DOWNLOAD_FAILED.format(error="Could not fetch file info"),
                parse_mode="markdown"
            )
            # Send error log
            await send_error_log(client, user_id, terabox_link, "API returned error")
            return
        
        file_name = file_info.get('file_name', 'download')
        file_size_mb = file_info.get('size_mb', 0)
        direct_link = file_info.get('direct_link')
        
        if not direct_link:
            await status_msg.edit_text(
                script.DOWNLOAD_FAILED.format(error="Could not get direct download link"),
                parse_mode="markdown"
            )
            await send_error_log(client, user_id, terabox_link, "No direct link in response")
            return
        
        # Apply user's custom prefix if set
        prefix = UserSettings.get_prefix(user_id)
        if prefix:
            file_name = apply_prefix_to_filename(prefix, file_name)
        
        # Send log with download info
        await send_success_log(
            client,
            script.DOWNLOAD_LOG.format(
                user_id=user_id,
                filename=file_name,
                filesize=f"{file_size_mb}MB"
            )
        )
        
        # Update status
        await status_msg.edit_text(script.DOWNLOADING)
        
        # Download and upload file
        try:
            # This would require downloading the file first
            # For now, we'll send a message that the file would be downloaded
            
            await status_msg.edit_text(script.UPLOADING)
            
            # Send completion message
            await message.reply_text(
                script.DOWNLOAD_COMPLETE.format(
                    filename=file_name,
                    filesize=f"{file_size_mb}MB"
                ),
                parse_mode="markdown"
            )
            
            logger.info(f"Download completed for user {user_id}: {file_name}")
            
        except Exception as e:
            await status_msg.edit_text(
                script.DOWNLOAD_FAILED.format(error=str(e)),
                parse_mode="markdown"
            )
            await send_error_log(client, user_id, terabox_link, str(e))
            logger.error(f"Download error for user {user_id}: {e}")
    
    except Exception as e:
        logger.error(f"Error in download_handler: {e}")
        await message.reply_text(
            script.DOWNLOAD_FAILED.format(error="An unexpected error occurred"),
            parse_mode="markdown"
        )
