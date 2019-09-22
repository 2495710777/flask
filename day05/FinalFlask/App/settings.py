


def get_database_uri(DATABASE):
    dialect = DATABASE.get('dialect') or 'mysql'
    driver = DATABASE.get('driver') or 'pymysql'
    username = DATABASE.get('username') or 'lwq'
    password = DATABASE.get('password') or '123123'
    host = DATABASE.get('host') or 'loaclhost'
    port = DATABASE.get('port') or '3306'
    database = DATABASE.get('database') or 'day051905'

    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect, driver, username, password, host, port, database)


class Config():
    Test = False
    Debug = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    Debug = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'lwq',
        'password': '123123',
        'host': 'localhost',
        'port': '3306',
        'database': 'day051905',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class TestConfig(Config):
    Test = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'lwq',
        'password': '123123',
        'host': 'localhost',
        'port': '3306',
        'database': 'day051905',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class ShowConfig(Config):

    Debug = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'lwq',
        'password': '123123',
        'host': 'localhost',
        'port': '3306',
        'database': 'day051905',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class ProductConfig(Config):

    Debug = True
    DATABASE = {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'lwq',
        'password': '123123',
        'host': 'localhost',
        'port': '3306',
        'database': 'day051905',
    }
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


ENV_NAME = {
    'develop': DevelopConfig,
    'test': TestConfig,
    'show': ShowConfig,
    'product': ProductConfig,
}
