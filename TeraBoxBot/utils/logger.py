import logging
import sys
from datetime import datetime

# Configure logging
def setup_logging():
    """Setup logging configuration"""
    log_format = '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    
    # Create logger
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('bot.log')
        ]
    )
    
    # Get logger for app
    logger = logging.getLogger(__name__)
    logger.info("Logging system initialized")
    return logger

# Setup logging when module is imported
logger = setup_logging()

def log_message(level: str, message: str, extra: dict = None):
    """
    Log a message with optional extra information
    
    Args:
        level: Log level (INFO, WARNING, ERROR, etc.)
        message: Message to log
        extra: Optional extra information dict
    """
    if extra:
        message = f"{message} | {extra}"
    
    if level.upper() == 'INFO':
        logger.info(message)
    elif level.upper() == 'WARNING':
        logger.warning(message)
    elif level.upper() == 'ERROR':
        logger.error(message)
    elif level.upper() == 'DEBUG':
        logger.debug(message)

def get_logger(name: str):
    """
    Get logger instance for a module
    
    Args:
        name: Module name
    
    Returns:
        Logger instance
    """
    return logging.getLogger(name)
