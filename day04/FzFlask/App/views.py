from flask import Blueprint, request

from App.models import db, Animal, Student

blue = Blueprint('blue', __name__)


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route(('/addUser/'))
def addUser():
    db.create_all()

    a = Animal()
    return '创建成功'


# =============================
# DML
# 增删改

# 增 添加一个对象
# 命名规范 动作加对象
@blue.route('/addStudent/')
def addStudent():
    s = Student()
    s.name = 'zs'
    s.age = 18
    db.session.add(s)
    db.session.commit()
    return '添加成功'


# 添加多个个对象
@blue.route('/addStudentList/')
def addStudentList():
    student_list = []
    for i in range(5):
        s = Student()
        s.name = '小明%d' % i
        s.age = i
        student_list.append(s)
    db.session.add_all(student_list)
    db.session.commit()
    return '添加成功'


# 删除
@blue.route('/deleteStudent/')
def deleteStudent():
    # 删除一定建立在查询之上
    s = Student.query.first()

    db.session.delete(s)
    db.session.commit()

    return '删除成功'


# 修改  查询基础上。设置之后直接添加提交
@blue.route('/updateStudent/')
def updateStudent():
    s = Student.query.first()

    s.name = 'ls'

    db.session.add(s)
    db.session.commit()
    return '修改成功'


# ===========================================
# 查询
# 获取单个数据 返回的数据类型是App.models.Student 类型 模型类
@blue.route('/getOne/')
def getOne():
    s = Student.query.first()
    print(s.name, s.age)
    print(type(s))
    # 没有last方法
    # s1 = Student.query.last()
    # print(s1.name, s1.age)
    s1 = Student.query.get(5)
    print(s1.name, s1.age)
    print(type(s1))
    return '查询成功'


# 单独的获取不到主键值，不使用不会报错
@blue.route('/getOne1/')
def getOne1():
    s = Student.query.get(10)
    return '查询成功'


# 获取结果集 all filter_by  filter
@blue.route('/getResult/')
def getResult():
    # all方法返回的是一个列表
    student_list = Student.query.all()
    print(type(student_list))
    for m in student_list:
        print(m.name, m.age)
        print(type(m))
    # =================================
    # filter_by 返回值类型是BaseQuery
    # 扩展
    #   flask =====>BaseQuery
    #   tornado =====>Query
    #   django =====> QuerySet

    # filter和fileter_by对主键字段的操作
    s1 = Student.query.filter_by(id=3)
    print(type(s1))
    # student_list = Student.query.filter(id==3)
    # print(type(student_list))

    # filter和fileter_by对非主键字段的操作
    # student_list = Student.query.filter_by(age = 3)
    # print(type(student_list))
    student_list = Student.query.filter(Student.age == 3)
    # print(type(student_list))

    # 条件查询
    # student_list = Student.query.filter(Student.age.__gt__(2))
    # student_list = Student.query.filter(Student.age.__lt__(2))
    # student_list = Student.query.filter(Student.age > 2)
    # student_list = Student.query.filter(Student.name.startswith('小'))
    # student_list = Student.query.filter(Student.name.endswith('1'))
    # student_list = Student.query.filter(Student.name.contains('小'))
    # student_list = Student.query.filter(Student.age.in_([1, 2]))
    for s in student_list:
        print(s.name, s.age)
    print(type(student_list))
    return '查询成功'

# ===================================================
@blue.route('/testFilter/')
def testFilter():
    # 排序
    # student_list = Student.query.order_by('age')
    # student_list = Student.query.order_by(db.desc('age'))
    # for s in student_list:
    #     print(s.name, s.age)
    # print(type(student_list))

    # limit 取出前几条数据
    # student_list = Student.query.limit(3)
    # for s in student_list:
    #     print(s.name, s.age)
    # print(type(student_list))
    # offset 去除前几个数据
    # student_list = Student.query.offset(3)
    # for s in student_list:
    #     print(s.name, s.age)
    # print(type(student_list))

    # 分页
    # 现在有五条数据  假如一页有两条，那么一共有3页
    # 要第二页的数据（limit, offset）
    # 总结： limit和offset无论谁先写,都是offset先执行
    # student_list = Student.query.limit(2).offset(2)
    # for s in student_list:
    #     print(s.name, s.age)

    # limit offset order_by
    # order_by 无论是语法和执行顺序都是先执行排序
    student_list = Student.query.order_by(db.desc('age')).limit(2).offset(2)
    for s in student_list:
        print(s.name, s.age)
    return '测试成功'
# =================================================
# 分页
#    原生代码
#     一页有几条数据  page_per/pagesize  第几页 page
@blue.route('/getPage/')
def getPage():
    page = int(request.args.get('page'))
    page_per = int(request.args.get('page_per'))

    # 第1页  2  0
    # 第2页  2  2
    # 第3页  2  4
    student_list = Student.query.limit(page_per).offset((page-1)*page_per)
    for s in student_list:
        print(s.name, s.age)
    return
