"""Command names and constants"""

# Commands
START_CMD = "start"
HELP_CMD = "help"
SET_PREFIX_CMD = "set_prefix"
VIEW_PREFIX_CMD = "view_prefix"
RESET_PREFIX_CMD = "reset_prefix"
SET_THUMBNAIL_CMD = "set_thumbnail"
VIEW_THUMBNAIL_CMD = "view_thumbnail"
REMOVE_THUMBNAIL_CMD = "remove_thumbnail"
BROADCAST_CMD = "broadcast"

# Command list for BotCommand
COMMANDS = [
    (START_CMD, "Show welcome message"),
    (HELP_CMD, "Show help and available commands"),
    (SET_PREFIX_CMD, "Set custom filename prefix"),
    (VIEW_PREFIX_CMD, "View your current prefix"),
    (RESET_PREFIX_CMD, "Reset to default naming"),
    (SET_THUMBNAIL_CMD, "Upload custom thumbnail"),
    (VIEW_THUMBNAIL_CMD, "View your custom thumbnail"),
    (REMOVE_THUMBNAIL_CMD, "Remove custom thumbnail"),
]
