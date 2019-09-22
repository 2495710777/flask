
# dielact+driver://username:password@host:port/database

def get_database_uri(DATABASE):

    dielact = DATABASE.get('dielact')
    driver = DATABASE.get('driver')
    username = DATABASE.get('username')
    password = DATABASE.get('password')
    host = DATABASE.get('host')
    port = DATABASE.get('port')
    database = DATABASE.get('database')

    return '{}+{}://{}:{}@{}:{}/{}'.format(dielact,driver,username,password,host,port,database)


class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopConfig(Config):

    DATABASE={
            'dielact':'mysql',
            'driver':'pymysql',
            'username':'lwq',
            'password':'123123',
            'host':'localhost',
            'port':'3306',
            'database':'day041905',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)



class TestConfig(Config):
    DATABASE = {
        'dielact': 'mysql',
        'driver': 'pymysql',
        'username': 'lwq',
        'password': '123123',
        'host': 'localhost',
        'port': '3306',
        'database': 'day041905',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


class ShowConfig(Config):
    DATABASE = {
        'dielact': 'mysql',
        'driver': 'pymysql',
        'username': 'lwq',
        'password': '123123',
        'host': 'localhost',
        'port': '3306',
        'database': 'day041905',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

class ProductConfig(Config):
    DATABASE = {
        'dielact': 'mysql',
        'driver': 'pymysql',
        'username': 'lwq',
        'password': '123123',
        'host': 'localhost',
        'port': '3306',
        'database': 'day041905',
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)