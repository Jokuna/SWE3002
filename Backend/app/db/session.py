from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB 연결 설정
MONGO_URI = "mongodb://admin:adminpass@localhost:27017/mydatabase?authSource=admin"
DATABASE_NAME = "mydatabase"

# MongoDB 클라이언트 및 접근
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
