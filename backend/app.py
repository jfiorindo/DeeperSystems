from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["deeper_db"]
collection = db["users"]

def serialize_user(user):
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
        "roles": user["roles"],
        "preferences": user["preferences"],
        "active": user["active"],
        "created_ts": user["created_ts"]
    }

@app.route("/users", methods=["GET"])
def get_users():
    users = list(collection.find())
    return jsonify([serialize_user(user) for user in users])

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return jsonify(serialize_user(user))
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    data["created_ts"] = datetime.utcnow().timestamp()
    result = collection.insert_one(data)
    user = collection.find_one({"_id": result.inserted_id})
    return jsonify(serialize_user(user)), 201

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
    if result.modified_count == 1:
        user = collection.find_one({"_id": ObjectId(user_id)})
        return jsonify(serialize_user(user))
    return jsonify({"error": "User not found or not modified"}), 404

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)