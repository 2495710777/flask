from flask import Flask
from flask_script import Manager

app = Flask(__name__)

# manager = Manager(app=app)
@app.route('/')
def hello():
    print('童年的荡秋千')
    print('说好不哭')
    return '右边画一道彩虹'


if __name__ == "__main__":
    # 默认情况下  _host = "127.0.0.1"
    #           _port = 5000
    # 如果要修改主机的端口号 可以在run中制定对应的参数
    # host是字符串类型 port可以使字符串或整数
    # pymysql里的端口号只能是整数
    app.run(port=8080, host='0.0.0.0',debug=True)
    # manager.run()
