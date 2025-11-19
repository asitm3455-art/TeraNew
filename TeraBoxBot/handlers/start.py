import logging
from pyrogram import Client, filters
from pyrogram.types import Message
import script
from database.user_settings import UserDatabase
from utils.logger import send_log

logger = logging.getLogger(__name__)

async def start_handler(client: Client, message: Message):
    """Handle /start command"""
    try:
        user = message.from_user
        
        # Add user to database
        UserDatabase.add_user(
            user_id=user.id,
            username=user.username or "Unknown",
            first_name=user.first_name or "",
            last_name=user.last_name or ""
        )
        
        # Send welcome message
        await message.reply_text(
            script.START_MESSAGE,
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        
        # Send log to log channel
        await send_log(
            client,
            script.USER_JOINED.format(
                user_id=user.id,
                username=user.username or "Unknown",
                first_name=user.first_name or "N/A"
            )
        )
        
        logger.info(f"User {user.id} started bot")
    except Exception as e:
        logger.error(f"Error in start_handler: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")

async def help_handler(client: Client, message: Message):
    """Handle /help command"""
    try:
        await message.reply_text(
            script.HELP_MESSAGE,
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        logger.info(f"User {message.from_user.id} requested help")
    except Exception as e:
        logger.error(f"Error in help_handler: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")
