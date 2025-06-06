from flask import Blueprint, render_template
from connection import Connection

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
    connection = Connection()

    profiles = connection.get_profiles()
    connection.close()

    return render_template("debug_info.html", rows=profiles)


# Gives all posts in database
@api.route("/posts")
def posts():
    connection = Connection()

    posts = connection.get_posts()
    connection.close()

    return render_template("debug_info.html", rows=posts)


# Gives all comments in database
@api.route("/comments")
def comments():
    connection = Connection()

    comments = connection.get_comments()
    connection.close()

    return render_template("debug_info.html", rows=comments)
