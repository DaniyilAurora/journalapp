from flask import Blueprint, render_template, request, redirect, url_for
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
    profiles_columns = connection.get_profiles_columns()
    connection.close()

    return render_template("debug_info.html", rows=profiles, information=profiles_columns, table_name="profiles")


# Adds new profile to a database
@api.route("/profiles/add", methods=['POST'])
def add_profile():
    connection = Connection()

    id = request.form['id'].strip()
    username = request.form['username'].strip()
    password = request.form['password'].strip()
    creation_date = request.form['creation_date'].strip()

    if id and username and password and creation_date:
        connection.add_profile(int(id), username, password, creation_date)
    connection.close()

    return redirect(url_for('api.profiles'))


# Deletes profile from a database
@api.route("/profiles/delete", methods=['POST'])
def delete_profile():
    connection = Connection()

    id = request.form['id'].strip()

    if id:
        connection.delete_profile(int(id))
    connection.close()

    return redirect(url_for('api.profiles'))


# Gives all posts in database
@api.route("/posts")
def posts():
    connection = Connection()

    posts = connection.get_posts()
    posts_columns = connection.get_posts_columns()
    connection.close()

    return render_template("debug_info.html", rows=posts, information=posts_columns, table_name="posts")


# Adds new post to a database
@api.route("/posts/add", methods=['POST'])
def add_post():
    connection = Connection()

    id = request.form['id'].strip()
    title = request.form['title'].strip()
    text = request.form['text'].strip()
    author_id = request.form['author_id'].strip()
    creation_date = request.form['creation_date'].strip()
    likes = request.form['likes'].strip()

    if id and title and text and author_id and creation_date and likes:
        connection.add_post(int(id), title, text, int(author_id), creation_date, int(likes))
    connection.close()

    return redirect(url_for('api.posts'))


# Deletes post from a database
@api.route("/posts/delete", methods=['POST'])
def delete_post():
    connection = Connection()

    id = request.form['id'].strip()

    if id:
        connection.delete_post(int(id))
    connection.close()

    return redirect(url_for('api.posts'))


# Gives all comments in database
@api.route("/comments")
def comments():
    connection = Connection()

    comments = connection.get_comments()
    comments_columns = connection.get_comments_columns()
    connection.close()

    return render_template("debug_info.html", rows=comments, information=comments_columns, table_name="comments")


# Adds new comment to a database
@api.route("/comments/add", methods=['POST'])
def add_comment():
    connection = Connection()

    id = request.form['id'].strip()
    text = request.form['text'].strip()
    likes = request.form['likes'].strip()
    author_id = request.form['author_id'].strip()
    post_id = request.form['post_id'].strip()
    creation_date = request.form['creation_date'].strip()

    if id and text and likes and author_id and post_id and creation_date:
        connection.add_comment(int(id), text, int(likes), int(author_id), int(post_id), creation_date)
    connection.close()

    return redirect(url_for('api.comments'))


# Deletes comment from a database
@api.route("/comments/delete", methods=['POST'])
def delete_comment():
    connection = Connection()

    id = request.form['id'].strip()

    if id:
        connection.delete_comment(int(id))
    connection.close()

    return redirect(url_for('api.comments'))
