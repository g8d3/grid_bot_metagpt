from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    bots = db.relationship('Bot', backref='user', lazy='dynamic')

    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Bot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String(64))
    symbol = db.Column(db.String(64))
    lower_price = db.Column(db.Float)
    upper_price = db.Column(db.Float)
    grid_levels = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, exchange: str, symbol: str, lower_price: float, upper_price: float, grid_levels: int, user: User):
        self.exchange = exchange
        self.symbol = symbol
        self.lower_price = lower_price
        self.upper_price = upper_price
        self.grid_levels = grid_levels
        self.user = user
