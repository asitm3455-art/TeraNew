import logging
import re
from pyrogram import Client, filters
from pyrogram.types import Message
import script
from database.user_settings import UserSettings

logger = logging.getLogger(__name__)

async def set_prefix_handler(client: Client, message: Message):
    """Handle /set_prefix command"""
    try:
        user_id = message.from_user.id
        
        # Extract prefix from command
        args = message.text.split(maxsplit=1)
        
        if len(args) < 2:
            # Ask user to provide prefix
            await message.reply_text(
                "📝 **Set Custom Prefix**\n\n"
                "Usage: `/set_prefix your_prefix`\n\n"
                "Example: `/set_prefix MyFiles_`",
                parse_mode="markdown"
            )
            return
        
        prefix = args[1].strip()
        
        # Validate prefix (only alphanumeric and underscore)
        if not re.match(r'^[a-zA-Z0-9_]{1,30}$', prefix):
            await message.reply_text(
                script.INVALID_PREFIX,
                parse_mode="markdown"
            )
            return
        
        # Save prefix to database
        success = UserSettings.set_prefix(user_id, prefix)
        
        if success:
            await message.reply_text(
                script.PREFIX_SET.format(prefix=prefix),
                parse_mode="markdown"
            )
            logger.info(f"Prefix set for user {user_id}: {prefix}")
        else:
            await message.reply_text("❌ Failed to save prefix. Please try again.")
    
    except Exception as e:
        logger.error(f"Error in set_prefix_handler: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")

async def view_prefix_handler(client: Client, message: Message):
    """Handle /view_prefix command"""
    try:
        user_id = message.from_user.id
        prefix = UserSettings.get_prefix(user_id)
        
        if not prefix:
            prefix = "(No custom prefix set)"
        
        await message.reply_text(
            script.PREFIX_VIEWED.format(prefix=prefix),
            parse_mode="markdown"
        )
        logger.info(f"User {user_id} viewed prefix")
    
    except Exception as e:
        logger.error(f"Error in view_prefix_handler: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")

async def reset_prefix_handler(client: Client, message: Message):
    """Handle /reset_prefix command"""
    try:
        user_id = message.from_user.id
        success = UserSettings.reset_prefix(user_id)
        
        if success:
            await message.reply_text(
                script.PREFIX_RESET,
                parse_mode="markdown"
            )
            logger.info(f"Prefix reset for user {user_id}")
        else:
            await message.reply_text("❌ Failed to reset prefix. Please try again.")
    
    except Exception as e:
        logger.error(f"Error in reset_prefix_handler: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")
