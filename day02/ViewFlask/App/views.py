import uuid

from flask import Blueprint, render_template, url_for, request, session, make_response, Response

# 初始化蓝图
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World'


# 对路由参数
# 基本结构  /资源路径/<变量>/
# 访问路径 http://127.0.0.1:5000/testRoute/1/
# 路由参数的名字视图函数的参数一致
# 路由参数传递到视图函数中  是字符串类型
@blue.route('/testRoute/<id>/')
def test(id):
    print(type(id))
    return 'testRoute'+id

# 路由参数的类型，默认情况是字符串
# string path int float uuid any

@blue.route("/testRoute1/<string:name>/")
def testRoute1(name):
    print(name)
    print(type(name))
    return 'testRoute1'+name

@blue.route('/testRoute2/<path:name>')
def testRoute2(name):
    print(name)
    print(type(name))
    return 'testRoute2'+name

# string 和 path 的区别
# string 遇到 / 会当作结束标签
# path 会把后面的整体当作字符串， 遇见 / 当作字符串中的一个

# int
@blue.route('/testRoute3/<int:money>/')
def testRoute3(money):
    print(money)
    print(type(money))
    return 'testRoute3'+str(money)

# float
@blue.route('/testRoute4/<float:price>/')
def testRoute4(price):
    print(price)
    print(type(price))
    return 'testRoute4'+str(price)

# uuid
@blue.route('/testuuid/')
def testuuid():
    uid = uuid.uuid4()
    print(uid)
    return 'testuuid'

@blue.route('/testRoute5/<uuid:uid>')
def testRoute5(uid):
    print(uid)
    print(type(uid))
    return 'testRoute5'


# any
@blue.route('/testRoute6/<any(a,b):p>/')
def testRoute6(p):
    print(p)
    print(type(p))
    return 'testRoute6'

# 请求方式又叫做http方法
# get(获取) post(添加) delete(删除)  put(修改全部) patch(修改部分属性)

# 需求：执行一个视图函数，跳转到一个模板 login.html
# 在模板中输入用户名字，然后点击登陆
# 点击之后 显示欢迎光临红浪漫

@blue.route('/toLogin/')
def tologin():
    return render_template('login.html')

# 浏览器路由请求方式，默认是 get head options,不支持post delete
# 想使用post delete put patch 使用methods=['post','put']
# 列表元素的大小写都可以
@blue.route('/login/', methods=['post'])
def login():
    return '欢迎光临红浪漫'

# 状态码
# 200 成功  数据传输没有丢失，浏览器完全接受
# 301 重定向
# 302 永久重定向
# 403 防跨战攻击 forbidden
# 404 路径错误
# 405 请求方式错误
# 500 服务器 业务逻辑错误

# postman 请求模拟工具
# 写了methods之后，就只能使用其中的请求方式，默认的get也不能使用
@blue.route('/testPostman/', methods=['post', 'get'])
def testPostman():
    return '我的梦想不是说说而已'


# 反向解析
@blue.route('/testReverse/')
def testReverse():
    return 'testReverse'

@blue.route('/testReverse1/')
def testReverse1():

    s = url_for('blue.testReverse')
    print(s)

    s1 = url_for('blue.testPostman')
    print(s1)
    # 应用场景
    #       1、redirect('/index/') ,重定向到index请求
    #           尽量不要使用硬编码 redirect(url_for('blue.index'))
    #       2、页面中 不要使用硬编码 form action='/login/'
    #           form action = url_for('blue.login')

    return 'testReverse1'

# ==========================
@blue.route('/testRequest/',methods=['post','get'])
def testRequest():
    # mysql 3306 mongodb 27017 oracle 1521 redis 6379
    # http 80  https 443
    # ftp 21 ssh 22
    # smtp 25 邮箱

    # 获取的是请求方式/http方法
    print(request.method)

    # 去掉请求参数的路径
    # 127.0.0.1:5000/testRequest/
    print(request.base_url)

    # 主机的路径不带请求资源路径
    # 127.0.0.1:5000/
    print(request.host_url)

    # 完整的url路径（请求资源路径，请求参数）
    # 127.0.0.1:5000/testRequest/?name=zs
    print(request.url)

    # 返回主机地址  应用场景 反爬虫
    print(request.remote_addr)

    # 应用场景 文件上传
    print(request.files)

    # 请求服务器带的数据，要符合服务器的要求
    # 请求头
    print(request.headers)

    # 请求资源路径 /testRequest/
    print(request.path)

    # 获取请求的cookies
    print(request.cookies)


    # http://127.0.0.1:5000/testRequest/?name=zs
    # 怎么获取name的值
    print(request.args)
    name = request.args.get('name')
    print(name)
    name1 = request.args.getlist('name')
    print(name1)

    # 参数名有多个相同的，遇见第一个返回
    age = request.args.get('age')
    print(age)
    # 全部需要用getlist()
    age1 = request.args.getlist('age')
    print(age1)

    #
    name2 = request.form.get('name')
    print(name2)

    age2 = request.form.get('age')
    print(age2)

    age3 = request.form.getlist('age')
    print(age3)

    return 'testRequest'

# ===========================================
# response返回值

# 视图函数返回字符串
@blue.route('/testResponse/')
def testResponse():
    return '离离原上草'

# 视图函数返回一个模板(html页面)
@blue.route('/testResponse2/')
def testResponse2():
    s = render_template('testResponse2.html')
    print(type(s))
    return s

# 视图函数返回一个make_response()
@blue.route('/testResponse3/')
def testResponse3():
    r = make_response('<h1>举头望明月</h1>')
    print(type(r))
    return r

# 视图函数返回重定向redirect
@blue.route('/index/')
def index():
    return 'welcome to 东北'

@blue.route('/testResponse4/')
def testResponse4():
    # return redirect('/index')
    r = redirect(url_for('blue.index'))
    return r

# 视图函数返回Response对象
@blue.route('/testResponse5/')
def testResponse5():
    r = Response('低头思故乡')
    return r

# ======================================
# 异常abort
@blue.route('/testAbort/')
def testAbort():
    abort(404)
    return 'testAbort'

@blue.errorhandler(404)
def testAbort1(Exception):
    return '系统正在升级，请稍候再试...'

# ======================================
# cookie的使用
# 需求：执行一个视图函数tologincookie，跳转到logincookie.html
#       输入用户名，点击提交 跳转到welcomecookie.html
#       该页面的内容是 欢迎xxx光临red romance...
#       如果没有登陆 直接跳转到welcomecookie.html,欢迎游客光临


# @blue.route('/tologincookie/')
# def tologincookie():
#     return render_template('logincookie.html')
#
# @blue.route('/logincookie/', methods=['post'])
# def logincookie():
#     name = request.form.get('name')
#
#     # response 是个对象
#     response = redirect(url_for('blue.welcomecookie'))
#     print(response)
#     response.set_cookie('name', name)
#
#     return response
#
#
# @blue.route('/welcomecookie/')
# def welcomecookie():
#     # 获取cookie中的name
#     name = request.cookies.get('name','游客')
#
#     return render_template('welcomecookie.html', name=name)
#
# @blue.route('/logoutcookie/')
# def logoutcookie():
#
#     response = redirect(url_for('blue.welcomecookie'))
#
#     response.delete_cookie('name')
#     return response

@blue.route('/tologincookie/')
def tologincookie():
    return render_template('logincookie.html')

@blue.route('/logincookie/', methods=['post'])
def logincookie():
    name = request.form.get('name')

    session['name'] = name
    print(name)
    return redirect(url_for('blue.welcomecookie'))


@blue.route('/welcomecookie/')
def welcomecookie():
    # 获取cookie中的name
    name = session.get('name', '游客')
    print(name)
    return render_template('welcomecookie.html', name=name)

@blue.route('/logoutcookie/')
def logoutcookie():
    resp = redirect(url_for('blue.welcomecookie'))
    resp.delete_cookie('session')
    # session.pop('name')
    return resp
