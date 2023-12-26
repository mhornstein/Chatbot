from flask import Flask
from api.routes.chat import chat_bp

app = Flask(__name__)

app.register_blueprint(chat_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
