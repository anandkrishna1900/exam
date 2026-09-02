# app.py - simple REST API with a blueprint, JSON, and token auth
from flask import Flask, Blueprint, jsonify, request
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)

# API blueprint - all routes start with /api
api = Blueprint('api', __name__)
auth = HTTPTokenAuth(scheme='Bearer')

# A simple fixed token (in a real app this would be generated per user)
TOKEN = 'mysecrettoken123'

# Data stored in a simple list of dictionaries (instead of a database)
posts = [
    {'id': 1, 'title': 'Hello API', 'body': 'First post'},
    {'id': 2, 'title': 'Second Post', 'body': 'Another one'}
]

# check the token --
@auth.verify_token
def verify_token(token):
    return token == TOKEN  # True if the token matches

# -- READ: list all posts (public) --
@api.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)  # serialize the list to JSON

# -- CREATE: add a post (protected by token) --
@api.route('/posts', methods=['POST'])
@auth.login_required
def add_post():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Bad Request'}), 400
    new_post = {
        'id': len(posts) + 1,
        'title': data['title'],
        'body': data.get('body', '')
    }
    posts.append(new_post)
    return jsonify(new_post), 201  # 201 Created

# register the blueprint and run
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
