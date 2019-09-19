from flask import Flask
from flask_session import Session


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '110'
    # 如果报错 No moudle named 'redis'   证明虚拟环境正宗没有redis模块
    # 需要手动安装 pip install redis
    # session生命周期是30天
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX']='flask'
    Session(app=app)
    return app