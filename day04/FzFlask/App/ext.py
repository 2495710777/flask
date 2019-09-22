from flask_migrate import Migrate
from flask_session import Session

from App.models import db



def init_ext(app):
    # flask-session
    app.config['SECRET_KEY'] = '110'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX'] = 'python1905'
    Session(app=app)

    # app.config.from_object(DevelopConfig)
    # flask-sqlalchemy
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lwq:123123@localhost:3306/day041905'
    # init_app一定要在初始化参数的下面
    db.init_app(app=app)

    # flask-migrate
    migrate = Migrate()
    migrate.init_app(app=app, db=db)