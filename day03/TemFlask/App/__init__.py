from flask import Flask

from App.models import db


def create_app():
    app = Flask(__name__)
    # dialect(方言)+drive(驱动)://username:password@host:port/database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lwq:123123@localhost:3306/day031905'
    # app.config['sqlalchemy_database_uri'] = 'mysql+pymysql://lwq:123123@localhost:3306/day031905'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # app.config['sqlalchemy_track_modifications']=False
    db.init_app(app=app)
    return app