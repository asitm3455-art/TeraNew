import logging
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import config

logger = logging.getLogger(__name__)

class Database:
    """MongoDB database handler"""
    
    def __init__(self):
        """Initialize MongoDB connection"""
        try:
            self.client = MongoClient(config.MONGO_URI, serverSelectionTimeoutMS=5000)
            # Test connection
            self.client.admin.command('ping')
            self.db = self.client[config.DB_NAME]
            logger.info("✅ Connected to MongoDB")
        except ServerSelectionTimeoutError:
            logger.error("❌ Failed to connect to MongoDB")
            raise
    
    def get_db(self):
        """Get database instance"""
        return self.db
    
    def close(self):
        """Close MongoDB connection"""
        self.client.close()
        logger.info("MongoDB connection closed")
    
    def create_indexes(self):
        """Create necessary database indexes"""
        # Create user collection with indexes
        users_collection = self.db['users']
        users_collection.create_index('user_id', unique=True)
        users_collection.create_index('username')
        
        # Create settings collection
        settings_collection = self.db['user_settings']
        settings_collection.create_index('user_id', unique=True)
        
        # Create broadcast collection
        broadcast_collection = self.db['broadcasts']
        broadcast_collection.create_index('created_at')
        
        logger.info("Database indexes created")

# Initialize global database instance
try:
    db_instance = Database()
    db_instance.create_indexes()
except Exception as e:
    logger.error(f"Database initialization failed: {e}")
    raise
