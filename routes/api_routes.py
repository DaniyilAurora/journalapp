from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')


# Incorrect request format
@api.route("/")
def incorrect_format():
    return "Incorrect Request Format.", 400


# Just hello
@api.route('/hello')
def hello():
    return "Hello from API!"
