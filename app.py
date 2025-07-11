from flask import Flask, render_template
from routes.api_routes import api
from database import Database
from connection import Connection

app = Flask(__name__)

# Register the blueprint from routes/api_routes.py
app.register_blueprint(api)

# Create a database instance
db = Database()


@app.route('/')
def home():
    # Get all posts to display
    connection = Connection()
    posts = connection.get_posts()

    # Returns usernames of the posts authors
    usernames = []
    for post in posts:
        author_id = int(post[3])
        usernames.append(str(connection.get_profile_username_by_id(author_id)[0]))

    return render_template("index.html", posts=posts, usernames=usernames)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
