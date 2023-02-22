from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from config import MONGO_DB

mongo = MongoCli(MONGO_DB)
db = mongo.Romeo
