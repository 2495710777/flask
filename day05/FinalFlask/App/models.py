from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))


# 一对多

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    children = db.relationship("Child", backref="parent", lazy=True)


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))


# 一对一
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))

    address = db.relationship('Address', backref='user', lazy=True, uselist=False)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    user_id = db.Column(db.ForeignKey('user.id'))


# 多对多
class User1(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_id = db.Column(db.ForeignKey(User1.id))
    m_id = db.Column(db.ForeignKey(Movie.id))

    num = db.Column(db.Integer, default=1)

class Movie1(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32))
    # 导演
    director = db.Column(db.String(32))
    # 领衔主演
    starring = db.Column(db.String(128))
    # 上映时间
    showtime = db.Column(db.String(128))
    # 简介
    brief = db.Column(db.String(256))
    # 时长
    duration = db.Column(db.String(128))