import json
from dataclasses import dataclass, asdict
from pymongo import MongoClient
from datetime import datetime

@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: list
    preferences: UserPreferences
    active: bool
    created_ts: float

def get_roles(user):
    roles = []
    if user.get("is_user_admin"):
        roles.append("admin")
    if user.get("is_user_manager"):
        roles.append("manager")
    if user.get("is_user_tester"):
        roles.append("tester")
    return roles

client = MongoClient("mongodb://localhost:27017/")
db = client["deeper_db"]
collection = db["users"]

with open("udata.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)["users"]

collection.delete_many({}) 

users = []
for entry in raw_data:
    user = User(
        username=entry["user"],
        password=entry["password"],
        roles=get_roles(entry),
        preferences=UserPreferences(timezone=entry["user_timezone"]),
        active=entry["is_user_active"],
        created_ts=datetime.strptime(entry["created_at"], "%Y-%m-%dT%H:%M:%SZ").timestamp()
    )
    users.append(asdict(user))

collection.insert_many(users)
print("✅ Data imported successfully.")