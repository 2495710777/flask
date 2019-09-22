from flask import Blueprint, render_template, request, session, redirect, url_for
from sqlalchemy.sql.elements import and_

from App.models import emp, db

blue = Blueprint('blue', __name__)


@blue.route('/login/', methods=['post', 'get'])
def login():
    username = request.form.get('username')
    password = request.form.get('pwd')
    # print(username)
    user = emp.query.filter(and_(emp.username == username, emp.pwd == password))
    if user.count() > 0:
        return redirect(url_for('blue.userList'))
    return render_template('login.html')


@blue.route('/toRegist/')
def toRegist():
    return render_template('regist.html')


@blue.route('/regist/', methods=['get', 'post'])
def regist():
    use = emp()
    use.username = request.form.get('username')
    use.name = request.form.get('name')
    use.pwd = request.form.get('pwd')
    print(use.pwd)
    use.age = request.form.get('age')
    use.sex = request.form.get('sex')
    use.phone = request.form.get('phone')
    use.ask = request.form.get('ask')
    db.session.add(use)
    db.session.commit()
    return redirect(url_for('blue.login'))


@blue.route('/userList/', methods=['post', 'get'])
def userList():
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page', 5)

    pagination = emp.query.paginate(page=page, per_page=per_page)
    return render_template('userList.html', pagination=pagination)


@blue.route('/userDetail/')
def userDetail():
    id = request.args.get('id')
    print(id)
    user = emp.query.filter(emp.id == id)[0]

    return render_template('userDetail.html', user=user)


@blue.route('/delUser/')
def delUser():
    did = request.args.get('did')
    user = emp.query.filter(emp.id == did)[0]
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('blue.userList'))


@blue.route('/toUpdateUser')
def toUpdateUser():
    id = request.args.get('id')
    user = emp.query.filter(emp.id == id)[0]

    return render_template('updateUser.html', user=user)


@blue.route('/updateUser/', methods=['get', 'post'])
def updateUser():
    id = request.args.get('id')
    user = emp.query.get(id)
    user.username = request.form.get('username')
    user.name = request.form.get('name')
    user.pwd = request.form.get('pwd')
    user.age = request.form.get('age')
    user.sex = request.form.get('sex')
    user.phone = request.form.get('phone')
    user.ask = request.form.get('ask')
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('blue.userList'))
