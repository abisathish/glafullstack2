# app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient
from werkzeug.security import check_password_hash
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

client = MongoClient('mongodb://localhost:27017/')
db = client['login_db']
users_collection = db['users']

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    user = users_collection.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Invalid credentials😞'})

if __name__ == '__main__':
    app.run(debug=True)
