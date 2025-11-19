import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "terabot_db")

# Channel IDs
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
ERRORS_CHANNEL = int(os.getenv("ERRORS_CHANNEL", "0"))
STORAGE_CHANNEL = int(os.getenv("STORAGE_CHANNEL", "0"))

# Owner ID
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# API Configuration
TERABOX_API = "https://teraapi.boogafantastic.workers.dev/play"

# Rate Limiting
MAX_REQUESTS_PER_MINUTE = int(os.getenv("MAX_REQUESTS_PER_MINUTE", "5"))
FLOODWAIT_TIMEOUT = int(os.getenv("FLOODWAIT_TIMEOUT", "60"))

# File size limits (in MB)
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "2048"))

# Validation - Only validate if not empty
try:
    if BOT_TOKEN and API_ID and API_HASH:
        # All required values present
        pass
    else:
        # Missing values - will be caught in bot.py with better error message
        pass
except Exception as e:
    print(f"Config error: {e}")
