# All bot messages, captions, and UI strings

# Start Command
START_MESSAGE = """
👋 **Welcome to TeraBox Downloader Bot!**

I can help you download files from Terabox links directly to Telegram.

**How to use:**
1. Send me a Terabox link
2. I'll fetch the file and upload it to you
3. You can set custom filename prefixes and thumbnails

**Features:**
✨ Fast downloads from Terabox
📝 Auto-rename files with custom prefix
🖼️ Custom thumbnail support
⚡ Anti-spam & rate limiting
📊 Progress bar during upload

Use /help for more details!
"""

# Help Command
HELP_MESSAGE = """
📚 **Help & Commands**

**Available Commands:**
/start - Show welcome message
/help - Show this help message
/set_prefix - Set custom filename prefix
/view_prefix - View your current prefix
/reset_prefix - Reset to default prefix
/set_thumbnail - Upload custom thumbnail
/view_thumbnail - View your current thumbnail
/remove_thumbnail - Remove custom thumbnail

**How to Download:**
Just send me a Terabox link like:
`https://www.terabox.com/s/xxx`

**Tips:**
• Custom prefix will be added to all your downloads
• Custom thumbnails work for video files
• Maximum file size: 2GB
• Files are stored in bot's storage channel

Need more help? Contact: @owner
"""

# Download Messages
DOWNLOADING = "⬇️ **Downloading your file...**\n\nPlease wait..."
UPLOADING = "⬆️ **Uploading to Telegram...**\n\nDon't close this chat!"
DOWNLOAD_COMPLETE = "✅ **Download Complete!**\n\nFile: `{filename}`\nSize: {filesize}"
DOWNLOAD_FAILED = "❌ **Download Failed!**\n\nError: {error}\n\nPlease check the link and try again."

# Prefix Messages
PREFIX_SET = "✅ **Prefix Updated!**\n\nYour new prefix: `{prefix}`\n\nAll future downloads will use this prefix."
PREFIX_VIEWED = "📝 **Your Current Prefix:**\n\n`{prefix}`"
PREFIX_RESET = "🔄 **Prefix Reset!**\n\nYour downloads will use default naming."
INVALID_PREFIX = "❌ **Invalid Prefix!**\n\nPrefix can only contain letters, numbers, and underscores.\nMax 30 characters."

# Thumbnail Messages
THUMBNAIL_SET = "🖼️ **Thumbnail Updated!**\n\nYour custom thumbnail has been saved."
THUMBNAIL_VIEWED = "🖼️ **Your Current Thumbnail:**"
THUMBNAIL_REMOVED = "🗑️ **Thumbnail Removed!**\n\nDefault thumbnails will be used."
SEND_THUMBNAIL = "📸 **Send Thumbnail Image**\n\nPlease send a photo to set as your custom thumbnail."
INVALID_THUMBNAIL = "❌ **Invalid File!**\n\nPlease send an image file (JPG, PNG, etc.)"

# Broadcast Messages
BROADCAST_START = "📢 **Broadcast Started**\n\nSending message to all users..."
BROADCAST_COMPLETE = "✅ **Broadcast Complete!**\n\nMessage sent to {count} users."
BROADCAST_PROMPT = "📝 **Send Broadcast Message**\n\nReply to this message with the content you want to broadcast to all users."
NOT_OWNER = "❌ **Access Denied!**\n\nOnly the bot owner can use this command."

# Error Messages
INVALID_LINK = "❌ **Invalid Link!**\n\nPlease send a valid Terabox link."
RATE_LIMITED = "⏱️ **Rate Limited!**\n\nYou're downloading too fast. Please wait {seconds} seconds before trying again."
FLOODWAIT = "⚠️ **Too Many Requests!**\n\nTelegram has rate-limited us. Waiting {seconds} seconds..."
FILE_TOO_LARGE = "📦 **File Too Large!**\n\nFile size: {size}MB\nMaximum allowed: 2GB"

# Log Messages
USER_JOINED = "👤 **New User Joined!**\n\nUser ID: {user_id}\nUsername: @{username}\nName: {first_name}"
DOWNLOAD_LOG = "📥 **Download Started**\n\nUser: {user_id}\nFile: {filename}\nSize: {filesize}"

# Status Messages
PROCESSING = "⏳ Processing..."
CHECKING_LINK = "🔍 Checking link..."
EXTRACTING_INFO = "📋 Extracting file information..."
