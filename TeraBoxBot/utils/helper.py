import logging
import os

logger = logging.getLogger(__name__)

def get_file_size_mb(file_path: str) -> float:
    """
    Get file size in MB
    
    Args:
        file_path: Path to file
    
    Returns:
        File size in MB
    """
    try:
        if not os.path.exists(file_path):
            return 0
        return os.path.getsize(file_path) / (1024 * 1024)
    except Exception as e:
        logger.error(f"Error getting file size: {e}")
        return 0

def apply_prefix_to_filename(prefix: str, filename: str) -> str:
    """
    Apply prefix to filename
    
    Args:
        prefix: Prefix to add
        filename: Original filename
    
    Returns:
        Prefixed filename
    """
    try:
        if not prefix or not filename:
            return filename
        
        # Split filename and extension
        name_parts = filename.rsplit('.', 1)
        
        if len(name_parts) == 2:
            name, ext = name_parts
            return f"{prefix}{name}.{ext}"
        else:
            return f"{prefix}{filename}"
    
    except Exception as e:
        logger.error(f"Error applying prefix: {e}")
        return filename

def format_file_size(size_bytes: int) -> str:
    """
    Format bytes to human readable size
    
    Args:
        size_bytes: Size in bytes
    
    Returns:
        Formatted size string
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f}{unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f}TB"

def is_valid_terabox_link(link: str) -> bool:
    """
    Validate if link is a valid Terabox link
    
    Args:
        link: URL to validate
    
    Returns:
        True if valid Terabox link, False otherwise
    """
    return 'terabox.com' in link.lower() and '/s/' in link.lower()

def extract_links_from_text(text: str) -> list:
    """
    Extract all URLs from text
    
    Args:
        text: Text containing URLs
    
    Returns:
        List of URLs
    """
    import re
    url_pattern = re.compile(
        r'https?://(?:www\.)?terabox\.com/s/[a-zA-Z0-9]+'
    )
    return url_pattern.findall(text)
