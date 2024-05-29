from flask import Flask
from routes.streaming_routes import streaming_routes

app = Flask(__name__)

app.register_blueprint(streaming_routes)

if __name__ == '__main__':
    app.run(debug=True)
