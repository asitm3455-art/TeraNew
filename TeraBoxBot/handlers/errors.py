import logging
from pyrogram import Client
from pyrogram.errors import PeerIdInvalid
import config

logger = logging.getLogger(__name__)

async def send_log(client: Client, log_message: str):
    """Send log message to LOG_CHANNEL"""
    try:
        await client.send_message(
            chat_id=config.LOG_CHANNEL,
            text=log_message,
            parse_mode="markdown",
            disable_web_page_preview=True
        )
    except PeerIdInvalid:
        logger.error(f"Invalid LOG_CHANNEL ID: {config.LOG_CHANNEL}")
    except Exception as e:
        logger.error(f"Failed to send log: {e}")

async def send_error_log(client: Client, user_id: int, link: str, error: str):
    """Send error log to ERRORS_CHANNEL"""
    try:
        error_message = f"""
❌ **Download Error**

**User ID:** {user_id}
**Link:** {link}
**Error:** {error}
"""
        await client.send_message(
            chat_id=config.ERRORS_CHANNEL,
            text=error_message,
            parse_mode="markdown",
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Failed to send error log: {e}")

async def send_success_log(client: Client, message: str):
    """Send success log to STORAGE_CHANNEL"""
    try:
        await client.send_message(
            chat_id=config.STORAGE_CHANNEL,
            text=message,
            parse_mode="markdown",
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Failed to send success log: {e}")
