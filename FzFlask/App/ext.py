from flask_session import Session

from App.models import db
from App.settings import DevelopConfig


def init_ext(app):
    # flask-session
    app.config['SECRET_KEY']='110'
    app.config['SESSION_TYPE']='redis'
    app.config['SESSION_KEY_PREFIX']='python1905'
    Session(app=app)


    # 如果参数的传递的是类  那么会将这个类变为一个对象  该对象就具备了 SQLALCHEMY_DATABASE_URI
    # 和 SQLALCHEMY_TRACK_MODIFICATIONS
    app.config.from_object(DevelopConfig)

    # flask-sqlalchemy
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1234@localhost:3306/day041905'
    # 注意 init_app方法 一定要在初始化参数的下面
    # 如果报错SQLALCHEMY_TRACK_MODIFICATIONS  那么要么是单词写错 要么是初始化没有在init_app方法之上
    db.init_app(app=app)