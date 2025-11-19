import logging

logger = logging.getLogger(__name__)

async def upload_progress_callback(current: int, total: int, message=None):
    """
    Callback function to show upload progress
    
    Args:
        current: Current bytes uploaded
        total: Total bytes to upload
        message: Message object to edit (optional)
    """
    try:
        percentage = (current / total) * 100 if total > 0 else 0
        
        # Create progress bar
        progress_bar = create_progress_bar(percentage)
        
        progress_text = f"""
⬆️ **Uploading to Telegram**

{progress_bar}

{percentage:.1f}% ({current / (1024*1024):.1f}MB / {total / (1024*1024):.1f}MB)
"""
        
        # Edit message every 5% progress
        if message and int(percentage) % 5 == 0:
            try:
                await message.edit_text(progress_text.strip(), parse_mode="markdown")
            except Exception as e:
                logger.debug(f"Could not update progress message: {e}")
    
    except Exception as e:
        logger.error(f"Error in upload_progress_callback: {e}")

def create_progress_bar(percentage: float, length: int = 20) -> str:
    """
    Create a visual progress bar
    
    Args:
        percentage: Progress percentage (0-100)
        length: Length of progress bar
    
    Returns:
        Progress bar string
    """
    filled = int((percentage / 100) * length)
    bar = '█' * filled + '░' * (length - filled)
    return f"[{bar}]"

async def download_progress_callback(current: int, total: int, message=None):
    """
    Callback function to show download progress
    
    Args:
        current: Current bytes downloaded
        total: Total bytes to download
        message: Message object to edit (optional)
    """
    try:
        percentage = (current / total) * 100 if total > 0 else 0
        
        # Create progress bar
        progress_bar = create_progress_bar(percentage)
        
        progress_text = f"""
⬇️ **Downloading from Terabox**

{progress_bar}

{percentage:.1f}% ({current / (1024*1024):.1f}MB / {total / (1024*1024):.1f}MB)
"""
        
        # Edit message every 5% progress
        if message and int(percentage) % 5 == 0:
            try:
                await message.edit_text(progress_text.strip(), parse_mode="markdown")
            except Exception as e:
                logger.debug(f"Could not update progress message: {e}")
    
    except Exception as e:
        logger.error(f"Error in download_progress_callback: {e}")
