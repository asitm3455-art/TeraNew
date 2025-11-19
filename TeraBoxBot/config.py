import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "8593002387:AAHDSfKf7VURo5HemGum4Nza-LmvqDBD8lU")
API_ID = int(os.getenv("API_ID", "21265734"))
API_HASH = os.getenv("API_HASH", "515aa3c7024f499d16e6a0ff563955e3")

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://gekasi8728:kingkhan@cluster0.ilgcdab.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.getenv("DB_NAME", "terabot_db")

# Channel IDs
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1003347866431"))
ERRORS_CHANNEL = int(os.getenv("ERRORS_CHANNEL", "-1003347866431")
STORAGE_CHANNEL = int(os.getenv("STORAGE_CHANNEL", "-1003347866431"))

# Owner ID
OWNER_ID = int(os.getenv("OWNER_ID", "8302560804"))

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
