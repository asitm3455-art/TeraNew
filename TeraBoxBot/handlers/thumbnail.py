import logging
from pyrogram import Client, filters
from pyrogram.types import Message
import script
from database.user_settings import UserSettings

logger = logging.getLogger(__name__)

async def set_thumbnail_handler(client: Client, message: Message):
    """Handle /set_thumbnail command - ask user to send thumbnail"""
    try:
        await message.reply_text(
            script.SEND_THUMBNAIL,
            parse_mode="markdown"
        )
        logger.info(f"User {message.from_user.id} initiated thumbnail setup")
    
    except Exception as e:
        logger.error(f"Error in set_thumbnail_handler: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")

async def process_thumbnail_photo(client: Client, message: Message):
    """Process photo upload as thumbnail"""
    try:
        user_id = message.from_user.id
        
        # Check if message contains a photo
        if not message.photo:
            await message.reply_text(script.INVALID_THUMBNAIL, parse_mode="markdown")
            return
        
        # Get the photo file_id
        photo = message.photo
        file_id = photo.file_id
        
        # Save to database
        success = UserSettings.set_thumbnail(user_id, file_id)
        
        if success:
            await message.reply_text(
                script.THUMBNAIL_SET,
                parse_mode="markdown"
            )
            logger.info(f"Thumbnail set for user {user_id}")
        else:
            await message.reply_text("❌ Failed to save thumbnail. Please try again.")
    
    except Exception as e:
        logger.error(f"Error processing thumbnail: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")

async def view_thumbnail_handler(client: Client, message: Message):
    """Handle /view_thumbnail command"""
    try:
        user_id = message.from_user.id
        file_id = UserSettings.get_thumbnail(user_id)
        
        if not file_id:
            await message.reply_text(
                "🖼️ **No Custom Thumbnail**\n\n"
                "You haven't set a custom thumbnail yet.\n"
                "Use /set_thumbnail to upload one!",
                parse_mode="markdown"
            )
            return
        
        # Send the thumbnail
        await message.reply_text(script.THUMBNAIL_VIEWED, parse_mode="markdown")
        await client.send_photo(
            chat_id=message.chat.id,
            photo=file_id,
            reply_to_message_id=message.id
        )
        logger.info(f"User {user_id} viewed thumbnail")
    
    except Exception as e:
        logger.error(f"Error in view_thumbnail_handler: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")

async def remove_thumbnail_handler(client: Client, message: Message):
    """Handle /remove_thumbnail command"""
    try:
        user_id = message.from_user.id
        success = UserSettings.remove_thumbnail(user_id)
        
        if success:
            await message.reply_text(
                script.THUMBNAIL_REMOVED,
                parse_mode="markdown"
            )
            logger.info(f"Thumbnail removed for user {user_id}")
        else:
            await message.reply_text("❌ Failed to remove thumbnail. Please try again.")
    
    except Exception as e:
        logger.error(f"Error in remove_thumbnail_handler: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")
