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


# Gives all profiles in database
@api.route("/profiles")
def profiles():
    return "profiles"


# Gives all posts in database
@api.route("/posts")
def posts():
    return "posts"


# Gives all comments in database
@api.route("/comments")
def comments():
    return "comments"
