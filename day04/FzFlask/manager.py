from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app
from App.views import blue

app = create_app('develop')

manager = Manager(app=app)

app.register_blueprint(blueprint=blue)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
