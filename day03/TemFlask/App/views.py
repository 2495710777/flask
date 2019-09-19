from flask import Blueprint, render_template

from App import db
from App.models import Animal

blue = Blueprint('blue', __name__)
@blue.route('/')
def hello_world():
    return 'hello'


# 模板的基本使用
@blue.route('/index/')
def index():
    # 优化：  1、页面接受   视图函数不传递
    #        2、页面不接受，视图函数传递
    return render_template('index.html', age=18, sex='n')

# 结构标签
@blue.route('/testTem/')
def teseTem():
    # return render_template('base_a.html')
    return render_template('base_b.html')

# 宏定义
@blue.route('/testMacro/')
def testMacro():
    # return render_template('base_a.html')
    return render_template('testMacro.html')

# 循环控制
@blue.route('/testFor/')
def testFor():
    score_list = [59, 67, 85, 40, 100]
    return render_template('testFor.html', score_list=score_list)

# 过滤器
@blue.route('/testFilter/')
def testFilter():
    code='asdfsfdsftrgr'
    code1='    ab  cd    '
    code2 = '<h1>abcd</h1>'
    code3 = ['good','world','hello','goodbye']
    return render_template('testFilter.html', code=code,
                           code1=code1, code2=code2,code3=code3)


# 通过模型创建表
@blue.route('/createTable/')
def createTable():
    db.create_all()
    return '创建成功'

# 通过模型删除表
@blue.route('/dropTable/')
def dropTable():
    db.drop_all()
    return '删除成功'

# 通过模型添加数据
@blue.route('/addanimal/')
def addanimal():
    a = Animal()
    a.name = 'hen'
    a.color = 'yellow'
    db.session.add(a)
    db.session.commit()
    return '添加成功'

@blue.route('/findall/')
def findall():
    animal_list = Animal.query.all()

    for animal in animal_list:
        print(animal.name)
    return '查询成功'
