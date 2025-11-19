"""
TeraBox Downloader Bot
A fully functional Telegram bot using Pyrogram for downloading files from Terabox
"""

import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.types import BotCommand

# Import configurations
import config
from utils.logger import setup_logging

# Import handlers
from handlers.start import start_handler, help_handler
from handlers.download import download_handler
from handlers.rename import set_prefix_handler, view_prefix_handler, reset_prefix_handler
from handlers.thumbnail import (
    set_thumbnail_handler, view_thumbnail_handler, 
    remove_thumbnail_handler, process_thumbnail_photo
)
from handlers.broadcast import broadcast_handler, process_broadcast_message
from handlers.commands import START_CMD, HELP_CMD, SET_PREFIX_CMD, VIEW_PREFIX_CMD
from handlers.commands import RESET_PREFIX_CMD, SET_THUMBNAIL_CMD, VIEW_THUMBNAIL_CMD
from handlers.commands import REMOVE_THUMBNAIL_CMD, BROADCAST_CMD

# Setup logging
logger = setup_logging()

# Initialize Pyrogram client
app = Client(
    name="terabox_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    workers=10,
    workdir="./session"
)

# ============================================================
# COMMAND HANDLERS
# ============================================================

@app.on_message(filters.command(START_CMD))
async def start_command(client, message):
    """Handle /start command"""
    await start_handler(client, message)

@app.on_message(filters.command(HELP_CMD))
async def help_command(client, message):
    """Handle /help command"""
    await help_handler(client, message)

@app.on_message(filters.command(SET_PREFIX_CMD))
async def set_prefix_command(client, message):
    """Handle /set_prefix command"""
    await set_prefix_handler(client, message)

@app.on_message(filters.command(VIEW_PREFIX_CMD))
async def view_prefix_command(client, message):
    """Handle /view_prefix command"""
    await view_prefix_handler(client, message)

@app.on_message(filters.command(RESET_PREFIX_CMD))
async def reset_prefix_command(client, message):
    """Handle /reset_prefix command"""
    await reset_prefix_handler(client, message)

@app.on_message(filters.command(SET_THUMBNAIL_CMD))
async def set_thumbnail_command(client, message):
    """Handle /set_thumbnail command"""
    await set_thumbnail_handler(client, message)

@app.on_message(filters.command(VIEW_THUMBNAIL_CMD))
async def view_thumbnail_command(client, message):
    """Handle /view_thumbnail command"""
    await view_thumbnail_handler(client, message)

@app.on_message(filters.command(REMOVE_THUMBNAIL_CMD))
async def remove_thumbnail_command(client, message):
    """Handle /remove_thumbnail command"""
    await remove_thumbnail_handler(client, message)

@app.on_message(filters.command(BROADCAST_CMD))
async def broadcast_command(client, message):
    """Handle /broadcast command (owner only)"""
    await broadcast_handler(client, message)

# ============================================================
# CONTENT HANDLERS
# ============================================================

@app.on_message(filters.photo)
async def photo_handler(client, message):
    """Handle photo uploads - for custom thumbnails"""
    await process_thumbnail_photo(client, message)

@app.on_message(filters.text & ~filters.command)
async def text_handler(client, message):
    """Handle text messages - check for Terabox links and broadcast"""
    from handlers.broadcast import broadcast_context
    
    user_id = message.from_user.id
    
    # Check if user is in broadcast mode
    if user_id in broadcast_context and broadcast_context[user_id].get('awaiting_message'):
        await process_broadcast_message(client, message)
    else:
        # Check for Terabox links
        await download_handler(client, message)

# ============================================================
# BOT STARTUP & SHUTDOWN
# ============================================================

async def setup_bot_commands():
    """Setup bot commands menu"""
    commands = [
        BotCommand(command=START_CMD, description="Start the bot"),
        BotCommand(command=HELP_CMD, description="Show help message"),
        BotCommand(command=SET_PREFIX_CMD, description="Set custom filename prefix"),
        BotCommand(command=VIEW_PREFIX_CMD, description="View your prefix"),
        BotCommand(command=RESET_PREFIX_CMD, description="Reset prefix"),
        BotCommand(command=SET_THUMBNAIL_CMD, description="Upload custom thumbnail"),
        BotCommand(command=VIEW_THUMBNAIL_CMD, description="View thumbnail"),
        BotCommand(command=REMOVE_THUMBNAIL_CMD, description="Remove thumbnail"),
    ]
    
    try:
        await app.set_bot_commands(commands)
        logger.info("Bot commands registered successfully")
    except Exception as e:
        logger.error(f"Failed to set bot commands: {e}")

async def on_startup():
    """Called when bot starts"""
    logger.info("=" * 50)
    logger.info("TeraBox Downloader Bot Starting...")
    logger.info("=" * 50)
    
    # Get bot info
    me = await app.get_me()
    logger.info(f"Bot Username: @{me.username}")
    logger.info(f"Bot ID: {me.id}")
    
    # Setup bot commands
    await setup_bot_commands()
    
    logger.info("✅ Bot is ready and listening for messages...")

async def on_shutdown():
    """Called when bot stops"""
    logger.info("=" * 50)
    logger.info("TeraBox Downloader Bot Shutting Down...")
    logger.info("=" * 50)

# ============================================================
# BOT STARTUP
# ============================================================

async def main():
    """Main function to run the bot"""
    try:
        # Run startup
        await on_startup()
        
        # Start the bot
        async with app:
            logger.info("Bot client started successfully")
            await app.idle()
    
    except KeyboardInterrupt:
        logger.info("Bot stopped by user (Ctrl+C)")
    
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise
    
    finally:
        await on_shutdown()

if __name__ == "__main__":
    logger.info("Starting TeraBox Downloader Bot...")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot interrupted by user")
    except ValueError as e:
        logger.error(f"❌ Configuration Error: {e}")
        logger.error("\n📝 Please check your .env file and make sure all required variables are set:")
        logger.error("   - BOT_TOKEN (from @BotFather)")
        logger.error("   - API_ID (from my.telegram.org)")
        logger.error("   - API_HASH (from my.telegram.org)")
        logger.error("   - LOG_CHANNEL (your channel ID)")
        logger.error("   - ERRORS_CHANNEL (your channel ID)")
        logger.error("   - STORAGE_CHANNEL (your channel ID)")
        logger.error("   - OWNER_ID (your user ID)")
        logger.error("\n📖 See GET_CREDENTIALS.md for detailed instructions")
        exit(1)
    except Exception as e:
        logger.critical(f"Critical error: {e}")
        exit(1)
