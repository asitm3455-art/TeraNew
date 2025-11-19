import logging
from pyrogram import Client, filters
from pyrogram.types import Message
import script
import config
from database.user_settings import UserDatabase

logger = logging.getLogger(__name__)

# State management for broadcast input
broadcast_context = {}

async def broadcast_handler(client: Client, message: Message):
    """Handle /broadcast command - owner only"""
    try:
        user_id = message.from_user.id
        
        # Check if user is owner
        if user_id != config.OWNER_ID:
            await message.reply_text(script.NOT_OWNER, parse_mode="markdown")
            logger.warning(f"Non-owner {user_id} attempted broadcast")
            return
        
        # Ask for broadcast message
        await message.reply_text(
            script.BROADCAST_PROMPT,
            parse_mode="markdown"
        )
        broadcast_context[user_id] = {'awaiting_message': True}
        logger.info(f"Owner {user_id} initiated broadcast")
    
    except Exception as e:
        logger.error(f"Error in broadcast_handler: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")

async def process_broadcast_message(client: Client, message: Message):
    """Process and send broadcast message to all users"""
    try:
        user_id = message.from_user.id
        
        # Check if user is owner and is in broadcast context
        if user_id != config.OWNER_ID or user_id not in broadcast_context:
            return
        
        if not broadcast_context[user_id].get('awaiting_message'):
            return
        
        # Remove from context
        del broadcast_context[user_id]
        
        # Get broadcast message
        broadcast_text = message.text or message.caption
        
        if not broadcast_text:
            await message.reply_text("❌ Invalid message format. Please try again.")
            return
        
        # Get all users
        users = UserDatabase.get_all_users()
        
        if not users:
            await message.reply_text("❌ No users in database.")
            return
        
        # Send status
        status_msg = await message.reply_text(script.BROADCAST_START, parse_mode="markdown")
        
        # Send to all users
        success_count = 0
        failed_count = 0
        
        for user_doc in users:
            try:
                user_id_to_send = user_doc['user_id']
                await client.send_message(
                    chat_id=user_id_to_send,
                    text=broadcast_text,
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                success_count += 1
            except Exception as e:
                logger.warning(f"Failed to send broadcast to {user_id_to_send}: {e}")
                failed_count += 1
        
        # Send completion message
        await status_msg.edit_text(
            script.BROADCAST_COMPLETE.format(count=success_count),
            parse_mode="markdown"
        )
        
        logger.info(f"Broadcast completed: {success_count} sent, {failed_count} failed")
    
    except Exception as e:
        logger.error(f"Error in process_broadcast_message: {e}")
        await message.reply_text(f"❌ An error occurred: {str(e)}")
