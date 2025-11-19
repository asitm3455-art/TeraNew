import logging
from datetime import datetime
from database.db import db_instance

logger = logging.getLogger(__name__)

class UserSettings:
    """Handle user-specific settings"""
    
    @staticmethod
    def set_prefix(user_id: int, prefix: str) -> bool:
        """Set custom filename prefix for user"""
        try:
            settings_col = db_instance.get_db()['user_settings']
            settings_col.update_one(
                {'user_id': user_id},
                {'$set': {
                    'user_id': user_id,
                    'prefix': prefix,
                    'updated_at': datetime.now()
                }},
                upsert=True
            )
            logger.info(f"Prefix set for user {user_id}: {prefix}")
            return True
        except Exception as e:
            logger.error(f"Error setting prefix: {e}")
            return False
    
    @staticmethod
    def get_prefix(user_id: int) -> str:
        """Get user's custom prefix or default"""
        try:
            settings_col = db_instance.get_db()['user_settings']
            settings = settings_col.find_one({'user_id': user_id})
            return settings.get('prefix', '') if settings else ''
        except Exception as e:
            logger.error(f"Error getting prefix: {e}")
            return ''
    
    @staticmethod
    def reset_prefix(user_id: int) -> bool:
        """Reset prefix to default (empty)"""
        try:
            settings_col = db_instance.get_db()['user_settings']
            settings_col.update_one(
                {'user_id': user_id},
                {'$set': {'prefix': '', 'updated_at': datetime.now()}},
                upsert=True
            )
            logger.info(f"Prefix reset for user {user_id}")
            return True
        except Exception as e:
            logger.error(f"Error resetting prefix: {e}")
            return False
    
    @staticmethod
    def set_thumbnail(user_id: int, file_id: str) -> bool:
        """Save user's custom thumbnail"""
        try:
            settings_col = db_instance.get_db()['user_settings']
            settings_col.update_one(
                {'user_id': user_id},
                {'$set': {
                    'user_id': user_id,
                    'thumbnail_file_id': file_id,
                    'updated_at': datetime.now()
                }},
                upsert=True
            )
            logger.info(f"Thumbnail set for user {user_id}")
            return True
        except Exception as e:
            logger.error(f"Error setting thumbnail: {e}")
            return False
    
    @staticmethod
    def get_thumbnail(user_id: int) -> str:
        """Get user's custom thumbnail file_id"""
        try:
            settings_col = db_instance.get_db()['user_settings']
            settings = settings_col.find_one({'user_id': user_id})
            return settings.get('thumbnail_file_id', '') if settings else ''
        except Exception as e:
            logger.error(f"Error getting thumbnail: {e}")
            return ''
    
    @staticmethod
    def remove_thumbnail(user_id: int) -> bool:
        """Remove user's custom thumbnail"""
        try:
            settings_col = db_instance.get_db()['user_settings']
            settings_col.update_one(
                {'user_id': user_id},
                {'$unset': {'thumbnail_file_id': ''}, '$set': {'updated_at': datetime.now()}},
                upsert=True
            )
            logger.info(f"Thumbnail removed for user {user_id}")
            return True
        except Exception as e:
            logger.error(f"Error removing thumbnail: {e}")
            return False

class UserDatabase:
    """Handle user data operations"""
    
    @staticmethod
    def add_user(user_id: int, username: str, first_name: str, last_name: str = "") -> bool:
        """Add or update user in database"""
        try:
            users_col = db_instance.get_db()['users']
            users_col.update_one(
                {'user_id': user_id},
                {'$set': {
                    'user_id': user_id,
                    'username': username,
                    'first_name': first_name,
                    'last_name': last_name,
                    'joined_at': datetime.now()
                }},
                upsert=True
            )
            logger.info(f"User {user_id} added/updated")
            return True
        except Exception as e:
            logger.error(f"Error adding user: {e}")
            return False
    
    @staticmethod
    def get_user(user_id: int) -> dict:
        """Get user information"""
        try:
            users_col = db_instance.get_db()['users']
            return users_col.find_one({'user_id': user_id}) or {}
        except Exception as e:
            logger.error(f"Error getting user: {e}")
            return {}
    
    @staticmethod
    def get_all_users() -> list:
        """Get all users (for broadcast)"""
        try:
            users_col = db_instance.get_db()['users']
            return list(users_col.find({}, {'user_id': 1}))
        except Exception as e:
            logger.error(f"Error getting all users: {e}")
            return []
