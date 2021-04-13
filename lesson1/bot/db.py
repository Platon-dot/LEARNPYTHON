from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://UncleStifler:HvaiLlnet29jIt5E@cluster0.o5qvo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
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