from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class emp(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64))
    name = db.Column(db.String(32))
    pwd = db.Column(db.String(32))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(8))
    phone = db.Column(db.String(11), unique=True)
    ask = db.Column(db.String(256))
