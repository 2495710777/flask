from flask import Blueprint, render_template, request, session, redirect, url_for
from sqlalchemy.sql.elements import or_, not_, and_

from App.models import Song, Parent, Child, db, Collection, Movie1

blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return 'sda'


# 分页封装
@blue.route('/getPageFz/')
def getPageFz():
    # paginate返回值类型pagination
    pagination = Song.query.paginate(2, 5).items
    # 不可以遍历
    print(pagination)
    print(type(pagination))
    for p in pagination:
        print(p.id, p.name)
    return '分页成功'


# =============================================================

# 逻辑
@blue.route('/getLogic')
def getLogic():
    # 与
    song = Song.query.filter(and_(Song.id==1,Song.name=='爱情买卖'))[0]
    # print(type(song))
    # print(song.id,song.name)
    #
    # # 或
    # song = Song.query.filter(or_(Song.id == 1, Song.name == '说好不哭'))[1]
    # print(type(song))
    # print(song.id, song.name)
    # 非
    # songs = Song.query.filter(not_(Song.id == 1))
    # print(type(songs))
    # for song in songs:
    #     print(song.id, song.name)
    # in
    songs = Song.query.filter(Song.id.in_([1, 2, 3, 4]))
    print(type(songs))
    for song in songs:
        print(song.id, song.name)
    return 'getLogic'


# ==========================================================

# 一对多
# 添加
@blue.route('/addParent/')
def addParent():
    parent = Parent()
    parent.name = '张三'

    child = Child()
    child.name = '张四'

    child1 = Child()
    child1.name = '王五'

    child_list = [child, child1]
    parent.children = child_list

    db.session.add(parent)
    db.session.commit()
    return '添加成功'


# 查询
# 主查从 给一个主表parent 然后查询child
@blue.route('/getChild/')
def getChild():
    childs = Child.query.filter(Parent.id == 1)
    for child in childs:
        print(child.name)
    return '查询成功'


# 从查主  给一个child  查询parent
@blue.route('/getParent/')
def getParent():
    parents = Parent.query.filter(Child.id > 1)
    for parent in parents:
        print(parent.name)
    return '查询成功'


@blue.route('/testRelation/')
def testRelation():
    parent = Parent.query.filter(Parent.id == 1)[0]
    child_list = parent.children
    for child in child_list:
        print(child.name)
    return '陈呢公共'


# 多对多
# 需求：第一次和会插入到数据库，第二次会在原来的基础上 数量加1
@blue.route('/addCollection/')
def addCollection():
    u_id = request.args.get('u_id')
    m_id = request.args.get('m_id')
    collections = Collection.query.filter(Collection.u_id == u_id).filter(Collection.m_id == m_id)

    # collection.count() 获取basequery的元素长度
    if collections.count() > 0:
        collection = collections[0]
        # +=1 效率没这个快
        collection.num = collection.num + 1
        db.session.add(collection)
        db.session.commit()
    else:
        collection = Collection()
        collection.u_id = u_id
        collection.m_id = m_id
    db.session.add(collection)
    db.session.commit()
    return '添加成功'

# ==================================
# flask-bootstrap
# <head>
#      head
#           title
#           metas
#           styles

# <body>
#       body
#           navbar
#           content
#           script
@blue.route('/bootstrapDemo/')
def bootstrapDemo():

    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page', 5)

    pagination = Movie1.query.paginate(page=page, per_page=per_page)
    return render_template('bootstrapDemo.html', pagination=pagination,page=page)

