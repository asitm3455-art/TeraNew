# TeraBox Downloader Bot

A fully functional Telegram bot built with Pyrogram that downloads files from Terabox links and uploads them directly to Telegram.

## Features

✨ **Core Features:**
- Download files from Terabox links via direct API
- Auto-rename feature with custom filename prefixes
- Custom thumbnail support for uploaded files
- Progress bars during downloads and uploads
- Anti-spam and rate limiting protection
- FloodWait handling for Telegram API limits

📊 **User Management:**
- Permanent user database using MongoDB
- User settings persistence (prefixes, thumbnails)
- Log channel for tracking new users
- Error tracking in separate channel
- Broadcast system for owner announcements

## Installation & Setup

### 1. Prerequisites
- Python 3.8+
- MongoDB (local or cloud)
- Telegram Bot Token
- Telegram API credentials (API_ID & API_HASH)

### 2. Clone & Setup

```bash
# Navigate to project directory
cd TeraBoxBot

# Install dependencies
pip install -r requirements.txt
```

### 3. Get Telegram Credentials

1. Create a bot via [@BotFather](https://t.me/botfather) on Telegram
2. Copy your `BOT_TOKEN`
3. Visit https://my.telegram.org/ and get your `API_ID` and `API_HASH`

### 4. Setup Environment Variables

```bash
# Copy example file
cp .env.example .env

# Edit .env and add your credentials
nano .env
```

Fill in the following:
- `BOT_TOKEN` - Your bot token from BotFather
- `API_ID` - From my.telegram.org
- `API_HASH` - From my.telegram.org
- `MONGO_URI` - MongoDB connection string
- `LOG_CHANNEL` - Channel ID for user join logs
- `ERRORS_CHANNEL` - Channel ID for error logs
- `STORAGE_CHANNEL` - Channel ID for download logs
- `OWNER_ID` - Your Telegram user ID (for broadcast commands)

### 5. Setup Logging Channels

1. Create 3 private channels (or use existing ones)
2. Add bot as administrator to all channels
3. Get channel IDs and add to .env file

To get channel ID:
- Send a message in the channel
- Forward it to [@userinfobot](https://t.me/userinfobot)
- Copy the channel ID (negative number)

### 6. Start the Bot

```bash
python bot.py
```

The bot will:
- Connect to MongoDB
- Register bot commands
- Start listening for messages
- Log startup information

## Usage

### User Commands

```
/start - Show welcome message
/help - Show help and available commands
/set_prefix <prefix> - Set custom filename prefix
/view_prefix - View your current prefix
/reset_prefix - Reset to default naming
/set_thumbnail - Upload custom thumbnail
/view_thumbnail - View your custom thumbnail
/remove_thumbnail - Remove custom thumbnail
```

### Owner Commands

```
/broadcast - Send message to all users (owner only)
```

### How to Download

Simply send a Terabox link to the bot:
```
https://www.terabox.com/s/xxxxx
```

The bot will:
1. Extract file information from the link
2. Download the file from Terabox
3. Apply your custom prefix (if set)
4. Upload to you with custom thumbnail (if set)
5. Log the action to storage channel

## Project Structure

```
TeraBoxBot/
├── bot.py                    # Main bot file with command handlers
├── config.py                 # Configuration and environment variables
├── script.py                 # All bot messages and UI strings
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment variables
│
├── database/
│   ├── __init__.py
│   ├── db.py                # MongoDB connection and initialization
│   └── user_settings.py     # User database and settings management
│
├── handlers/
│   ├── __init__.py
│   ├── start.py             # /start and /help commands
│   ├── download.py          # Main Terabox downloader logic
│   ├── commands.py          # Command definitions
│   ├── rename.py            # Prefix management handlers
│   ├── thumbnail.py         # Thumbnail handlers
│   ├── broadcast.py         # Owner broadcast system
│   └── errors.py            # Error logging functions
│
└── utils/
    ├── __init__.py
    ├── api.py               # Terabox API interaction
    ├── progress.py          # Progress bar functionality
    ├── helper.py            # Utility helper functions
    └── logger.py            # Logging configuration
```

## API Configuration

The bot uses this API to fetch Terabox file information:

```
https://teraapi.boogafantastic.workers.dev/play?url=YOUR_LINK
```

**API Response Format:**
```json
{
  "status": "success",
  "file_name": "filename.ext",
  "size": "100MB",
  "direct_link": "https://..."
}
```

## Database Schema

### Users Collection
```json
{
  "user_id": 123456789,
  "username": "username",
  "first_name": "John",
  "last_name": "Doe",
  "joined_at": "2024-01-01T12:00:00"
}
```

### User Settings Collection
```json
{
  "user_id": 123456789,
  "prefix": "MyPrefix_",
  "thumbnail_file_id": "file_id_here",
  "updated_at": "2024-01-01T12:00:00"
}
```

## Error Handling

The bot includes:
- Rate limiting (5 requests/minute per user)
- FloodWait handling (60-second timeout)
- Invalid link detection
- API error handling
- File size validation
- Database error recovery

## Logging

Logs are stored in two places:
1. **Console output** - Real-time logs during execution
2. **bot.log file** - Persistent log file for debugging

## Troubleshooting

### Bot doesn't start
- Check if all environment variables are set in .env
- Verify MongoDB connection with `mongosh`
- Check if BOT_TOKEN is valid

### Users can't download
- Verify Terabox links are valid and shareable
- Check if API is accessible (test URL manually)
- Ensure storage channel ID is correct

### MongoDB connection fails
- Verify MONGO_URI is correct
- Check if MongoDB service is running
- For cloud MongoDB, ensure IP is whitelisted

## Performance Tips

1. **Use MongoDB Atlas** for better reliability
2. **Set MAX_REQUESTS_PER_MINUTE** to prevent abuse
3. **Monitor bot.log** for errors
4. **Use /broadcast** cautiously (sends to all users)
5. **Keep bot session files** in a safe directory

## Security

- Never commit `.env` file to version control
- Keep BOT_TOKEN and API credentials private
- Use strong MongoDB passwords
- Add IP whitelist for MongoDB if cloud-hosted
- Validate all user inputs before processing

## Support & Issues

For issues or questions:
1. Check logs: `tail -f bot.log`
2. Verify all environment variables
3. Test API manually: `curl "https://teraapi.boogafantastic.workers.dev/play?url=LINK"`
4. Check Telegram bot API status

## License

This project is open source. Modify and distribute as needed.

## Author

Created for easy Terabox file downloading via Telegram

---

**Last Updated:** November 2024
**Python Version:** 3.8+
**Pyrogram Version:** 2.0+
