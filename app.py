from flask import Flask, jsonify
from pymongo import MongoClient
import certifi
ca = certifi.where()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "HOME"


client = MongoClient("mongodb+srv://kazanj7:nMGMWknI8ncDHz5M@cluster0.fslzo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsCAFile=ca)
db = client['LS3FALL2024']
users_collection = db['Users']

print(users_collection)

@app.route('/users', methods=['GET'])
def get_users():
    users = list(users_collection.find())
    users = []
    for user in users_collection.find():
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users)
if __name__ == '__main__':
    app.run(debug=True)
    





