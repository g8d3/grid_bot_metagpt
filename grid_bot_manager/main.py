## main.py
import os
from flask import Flask
from flask_login import LoginManager
from grid_bot_manager.models import db
from grid_bot_manager.views import bot_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:////tmp/test.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret-key')
    
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    app.register_blueprint(bot_blueprint)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
