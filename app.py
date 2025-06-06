from flask import Flask
from routes.api_routes import api

app = Flask(__name__)

# Register the blueprint from routes/api_routes.py
app.register_blueprint(api)


@app.route('/')
def home():
    return "Main page"


if __name__ == '__main__':
    app.run(debug=True)
