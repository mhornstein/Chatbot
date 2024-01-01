from flask import Flask
from api.routes.chat import chat_bp
from api.routes.upload import upload_bp

app = Flask(__name__)

app.register_blueprint(chat_bp, url_prefix='/')
app.register_blueprint(upload_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
