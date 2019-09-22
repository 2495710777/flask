from flask import Blueprint

from App.models import db

blue = Blueprint('blue', __name__)
@blue.route('/')
def hello_world():
    return 'Hello World!'

@blue.route('/createUser/')
def create_user():
    a = db.create_all()

    return '创建成功'