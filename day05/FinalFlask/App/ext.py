from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_session import Session

from App.models import db


def init_ext(app):
    # flask-session
    app.config['SECRET_KEY'] = '119'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX'] = 'flask1905'
    Session(app=app)

    # sqlalchemy
    db.init_app(app=app)

    # flask-migrate
    migrate = Migrate()
    migrate.init_app(app=app, db=db)

    # flask-bootstrap
    Bootstrap(app=app)

    # flask-debugtoolbar
    app.debug = True
    debugtoolbar = DebugToolbarExtension()
    debugtoolbar.init_app(app=app)
