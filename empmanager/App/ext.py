from flask_migrate import Migrate
from flask_session import Session

from App.models import db


def init_ext(app):
    app.config['SECRET_KEY']='110'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX'] = 'empmanager'
    Session(app=app)

    db.init_app(app=app)

    migrate = Migrate()
    migrate.init_app(app=app, db=db)

