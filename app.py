from flask import Flask, render_template
from routes.api_routes import api
from database import Database

app = Flask(__name__)

# Register the blueprint from routes/api_routes.py
app.register_blueprint(api)

# Create a database instance
db = Database()


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
