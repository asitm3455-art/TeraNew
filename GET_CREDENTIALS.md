# 🔑 How to Get Your Environment Variables

Follow this guide to obtain all required credentials for your bot.

---

## 1️⃣ BOT_TOKEN - From @BotFather

### Steps:
1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Click "Start" or send `/start`
3. Send `/newbot`
4. Choose a name for your bot (e.g., "TeraBox Downloader")
5. Choose a username for your bot (must end with "bot", e.g., "terabox_dl_bot")
6. BotFather will give you a token like: `123456789:ABCdefGHIjklmNOpqrsTUVwxyz`
7. Copy this token to `BOT_TOKEN` in .env

**Example:**
```
BOT_TOKEN=123456789:ABCdefGHIjklmNOpqrsTUVwxyz
```

---

## 2️⃣ API_ID & API_HASH - From my.telegram.org

### Steps:
1. Go to https://my.telegram.org/
2. Click "Sign in" with your phone number
3. Enter your phone number in international format (e.g., +1234567890)
4. Click "Next" and complete the login
5. Click on "API development tools" (left sidebar)
6. Fill in the form:
   - App title: "TeraBox Bot"
   - Short name: "terabox_bot"
   - URL: (leave blank)
   - Platform: Desktop (or your platform)
7. Click "Create application"
8. Copy your `api_id` and `api_hash`

**Example:**
```
API_ID=1234567
API_HASH=abcdef1234567890abcdef1234567890
```

---

## 3️⃣ OWNER_ID - Your Telegram User ID

### Method 1: Using @userinfobot
1. Open Telegram
2. Search for [@userinfobot](https://t.me/userinfobot)
3. Click "Start" or send any message
4. Bot will show your User ID like: `Your ID: 123456789`
5. Copy this number

### Method 2: Using @IDBot
1. Open Telegram
2. Search for [@IDBot](https://t.me/userinfobot)
3. Send `/start`
4. It will show your ID

**Example:**
```
OWNER_ID=123456789
```

---

## 4️⃣ Channel IDs - For Logging & Storage

You need to create 3 private channels:

### Create Channels:
1. Open Telegram
2. Click "+" → "New Group"
3. Select "Create a supergroup"
4. Enter channel name (e.g., "TeraBot Logs")
5. Make it private
6. Click "Create"
7. Go to channel info and add bot as administrator

### Get Channel ID:

**Method 1: Using @userinfobot**
1. In the channel, send a message
2. Forward that message to [@userinfobot](https://t.me/userinfobot)
3. Bot shows: `"Chat ID": -100123456789`
4. Copy the Chat ID (with the minus sign)

**Method 2: Automatic (First Run)**
1. Run the bot once
2. It will try to send logs and fail
3. Check bot.log for the actual channel ID needed

### The 3 Channels You Need:

1. **LOG_CHANNEL** - User join logs
   - Example: `-100123456789`

2. **ERRORS_CHANNEL** - Failed downloads
   - Example: `-100987654321`

3. **STORAGE_CHANNEL** - Download logs
   - Example: `-100555666777`

**Example:**
```
LOG_CHANNEL=-100123456789
ERRORS_CHANNEL=-100987654321
STORAGE_CHANNEL=-100555666777
```

---

## 5️⃣ MONGO_URI - MongoDB Connection

### Option A: Local MongoDB
```
MONGO_URI=mongodb://localhost:27017
```

### Option B: MongoDB Atlas (Cloud - Recommended)

1. Go to https://www.mongodb.com/cloud/atlas
2. Sign up (free account)
3. Create a new cluster (free tier)
4. Click "Connect"
5. Choose "Connect your application"
6. Copy the connection string
7. Replace `<username>` and `<password>`

**Example:**
```
MONGO_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

---

## 📝 Complete .env File Example

```env
# Telegram Bot Credentials
BOT_TOKEN=123456789:ABCdefGHIjklmNOpqrsTUVwxyz
API_ID=1234567
API_HASH=abcdef1234567890abcdef1234567890

# MongoDB Configuration
MONGO_URI=mongodb+srv://user:password@cluster0.xxxxx.mongodb.net/
DB_NAME=terabot_db

# Channel IDs (must be negative numbers with -100 prefix)
LOG_CHANNEL=-100123456789
ERRORS_CHANNEL=-100987654321
STORAGE_CHANNEL=-100555666777

# Owner ID (your Telegram user ID)
OWNER_ID=123456789

# Rate Limiting Settings
MAX_REQUESTS_PER_MINUTE=5
FLOODWAIT_TIMEOUT=60

# File Size Limits (in MB)
MAX_FILE_SIZE=2048
```

---

## ✅ Verification Checklist

After filling .env:

- [ ] BOT_TOKEN is not empty and contains a colon
- [ ] API_ID is a 7-10 digit number
- [ ] API_HASH is a 32-character string
- [ ] OWNER_ID is your Telegram user ID (9-10 digits)
- [ ] LOG_CHANNEL starts with -100
- [ ] ERRORS_CHANNEL starts with -100
- [ ] STORAGE_CHANNEL starts with -100
- [ ] MONGO_URI contains connection string
- [ ] All channels exist and bot is admin
- [ ] MongoDB is accessible

---

## 🧪 Test Your Credentials

```bash
# Check if .env is valid
cat .env | grep -E "BOT_TOKEN|API_ID|API_HASH"

# Run bot to test
cd TeraBoxBot
python bot.py
```

If bot starts without errors, everything is configured correctly!

---

## ⚠️ Security Tips

- **Never** commit .env to git
- **Never** share your BOT_TOKEN publicly
- **Never** share your API_HASH
- Keep OWNER_ID secret
- Use strong MongoDB password
- Enable IP whitelist on MongoDB Atlas

---

## 🆘 Troubleshooting

### "Invalid API ID or HASH"
- Double-check API_ID and API_HASH from my.telegram.org
- Make sure there are no extra spaces

### "Bot token is invalid"
- Regenerate token from @BotFather
- Copy the full token including the colon

### "Can't connect to MongoDB"
- Check MONGO_URI syntax
- Verify MongoDB is running: `systemctl status mongodb`
- Check MongoDB Atlas IP whitelist

### "Channel ID not found"
- Verify channel ID format (should start with -100)
- Make sure bot is admin in the channel
- Forward message to @userinfobot again

---

## 📞 Need Help?

1. Check if all variables are filled in .env
2. Look at bot.log for error messages
3. Verify each credential individually
4. Check GitHub issues for similar problems

---

Generated: November 19, 2024
