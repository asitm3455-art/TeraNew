#!/usr/bin/env python3
"""
Check if .env file is properly configured
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

print("\n" + "="*60)
print("🔍 CHECKING .env FILE CONFIGURATION")
print("="*60 + "\n")

# Check each required variable
checks = {
    "BOT_TOKEN": os.getenv("BOT_TOKEN"),
    "API_ID": os.getenv("API_ID"),
    "API_HASH": os.getenv("API_HASH"),
    "MONGO_URI": os.getenv("MONGO_URI"),
    "LOG_CHANNEL": os.getenv("LOG_CHANNEL"),
    "ERRORS_CHANNEL": os.getenv("ERRORS_CHANNEL"),
    "STORAGE_CHANNEL": os.getenv("STORAGE_CHANNEL"),
    "OWNER_ID": os.getenv("OWNER_ID"),
}

all_good = True

for key, value in checks.items():
    if value:
        # Show masked value for security
        if len(str(value)) > 20:
            masked = str(value)[:10] + "..." + str(value)[-5:]
        else:
            masked = value
        print(f"✅ {key:20} = {masked}")
    else:
        print(f"❌ {key:20} = NOT SET")
        all_good = False

print("\n" + "="*60)

if all_good:
    print("✅ ALL SETTINGS CORRECT! Bot should start now.")
    print("="*60 + "\n")
    print("Run: python bot.py")
else:
    print("❌ MISSING SETTINGS! Please edit your .env file.")
    print("="*60 + "\n")
    print("Required settings:")
    print("  1. BOT_TOKEN - Get from @BotFather on Telegram")
    print("  2. API_ID - Get from https://my.telegram.org")
    print("  3. API_HASH - Get from https://my.telegram.org")
    print("  4. MONGO_URI - MongoDB connection string")
    print("  5. LOG_CHANNEL - Your logging channel ID")
    print("  6. ERRORS_CHANNEL - Your errors channel ID")
    print("  7. STORAGE_CHANNEL - Your storage channel ID")
    print("  8. OWNER_ID - Your Telegram user ID")
    print("\nSee: GET_CREDENTIALS.md for step-by-step instructions")

print()
