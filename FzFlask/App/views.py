from flask import Blueprint

from App.models import User, db

blue = Blueprint('blue',__name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'



@blue.route('/addUser/')
def addUser():
    db.create_all()

    return '创建成功'