from pymongo import MongoClient
import settings

client = MongoClient(
    settings.API_MONGO
)

db = client.testdb

data = {
    "name": "Грэм Чепмен",
    "chat_id": 12345,
    "messages": [
        {"id": 1, "text": "Стой! Как тебя зовут?"},
        {"id": 2, "text": "Перед тобой Артур, король бриттов."}
    ]
}

db.testcolection.insert_one(data)