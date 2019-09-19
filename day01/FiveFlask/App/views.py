from flask import Blueprint


blue = Blueprint('first', __name__)
# print(__name__)


@blue.route('/index/')
def index():
    return '右边画一道彩虹'
