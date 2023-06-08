from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_flask_application():
        return 'Welcome to first python-Flask application'
