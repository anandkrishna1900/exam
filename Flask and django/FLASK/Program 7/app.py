# app.py - a small application to be tested
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/api/data')
def data():
    return jsonify({'name': 'Sahan', 'course': 'BCA'})

@app.route('/square/<int:number>')
def square(number):
    return jsonify({'number': number, 'square': number * number})

if __name__ == '__main__':
    app.run(debug=True)
