import logging
import aiohttp
import config

logger = logging.getLogger(__name__)

async def get_terabox_download_link(terabox_url: str) -> dict:
    """
    Fetch file information from Terabox API
    
    Args:
        terabox_url: The Terabox sharing link
    
    Returns:
        Dictionary with file_name, size_mb, and direct_link
    """
    try:
        # Build API URL
        api_url = f"{config.TERABOX_API}?url={terabox_url}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                if response.status != 200:
                    logger.error(f"API returned status {response.status}")
                    return {'error': f'API Error: {response.status}'}
                
                data = await response.json()
                
                # Check for errors in response
                if data.get('status') != 'success':
                    logger.error(f"API returned error: {data.get('error', 'Unknown')}")
                    return {'error': data.get('error', 'API Error')}
                
                # Extract file information
                result = {
                    'file_name': data.get('file_name', 'download'),
                    'size_mb': convert_size_to_mb(data.get('size', '0')),
                    'direct_link': data.get('direct_link', ''),
                }
                
                logger.info(f"Successfully fetched: {result['file_name']}")
                return result
    
    except aiohttp.ClientError as e:
        logger.error(f"Network error while calling API: {e}")
        return {'error': f'Network Error: {str(e)}'}
    
    except Exception as e:
        logger.error(f"Error calling Terabox API: {e}")
        return {'error': str(e)}

def convert_size_to_mb(size_str: str) -> float:
    """
    Convert size string (with units) to MB
    
    Args:
        size_str: Size string like "100MB", "2GB", etc.
    
    Returns:
        Size in MB as float
    """
    try:
        size_str = str(size_str).strip().upper()
        
        if 'GB' in size_str:
            return float(size_str.replace('GB', '')) * 1024
        elif 'MB' in size_str:
            return float(size_str.replace('MB', ''))
        elif 'KB' in size_str:
            return float(size_str.replace('KB', '')) / 1024
        elif 'B' in size_str:
            return float(size_str.replace('B', '')) / (1024 * 1024)
        else:
            # Try to parse as bytes
            return float(size_str) / (1024 * 1024)
    
    except Exception as e:
        logger.warning(f"Could not parse size: {size_str}. Error: {e}")
        return 0.0
