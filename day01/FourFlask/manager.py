from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app=app)
@app.route('/')
def hello():
    print('童年的荡秋千')
    print('说好不哭')
    return '右边画一道彩虹'


# 如果路由的格式是'/index/' 那么请求资源路径是127.0.0.1:5000/index
# 或者127.0.0.1:5000/index/
@app.route('/index/')
def index():
    return 'index'

# 如果路由的格式是'/index' 那么请求资源路径是127.0.0.1:5000/index,
# 不加/,加了会报404错误
@app.route('/index1')
def index1():
    return 'index1'

# 试图函数的返回值必须是字符串、字典、元组、response对象
@app.route('/testreturn/')
def testreturn():
    # 不可以是整数
    # return 1
    return '1'

# 执行视图函数 然后跳转到一个页面
@app.route('/testreturn1/')
def testreturn1():
    # render_template方法返回的是字符串
    s = render_template('testreturn1.html')
    print(type(s))
    return s

# 在模板中引用静态文件


if __name__ == "__main__":
    # 默认情况下  _host = "127.0.0.1"
    #           _port = 5000
    # 如果要修改主机的端口号 可以在run中制定对应的参数
    # host是字符串类型 port可以使字符串或整数
    # pymysql里的端口号只能是整数
    # app.run(port=8080, host='0.0.0.0',debug=True)
    manager.run()
