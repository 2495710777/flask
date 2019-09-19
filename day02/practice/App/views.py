import uuid

from flask import Blueprint, render_template, request, url_for, session

# from werkzeug.utils import redirect
from werkzeug.utils import redirect

blue = Blueprint('blue', __name__)

# @blue.route('/toLoginCookie/')
# def toLoginCookie():
#     return render_template('logincookie.html')
#
# @blue.route('/loginCookie/')
# def loginCookie():
#     name = request.form.get('name')
#     print(name)
#     return render_template('welcomecookie.html', name=name)

@blue.route('/testString/<string:id>')
def testString(id):
    print(type(id))
    return 'hello'+id

@blue.route('/testPath/<path:name>')
def testPath(name):
    print(type(name))
    return name

@blue.route('/testInt/<int:id>')
def testInt(id):
    print(type(id))
    return str(id)

@blue.route('/testFloat/<float:id>')
def testFloat(id):
    print(type(id))
    return str(id)

@blue.route('/testuuid/')
def testuuid():
    num = uuid.uuid4()
    print(num)
    return str(num)

@blue.route('/testuuid1/<uuid:id>')
def testuuid1(id):
    print(type(id))
    return str(id)

@blue.route('/testany/<any(a,b,c):p>/')
def testany(p):
    return p

@blue.route('/testPost/', methods=['post','get','put'])
def testPost():
    return 'sdsdsdsd'


@blue.route('/dskfugsdgb/',methods=['get','post','put'])
def hehe():
    return 'hehe'

@blue.route('/testReverse/')
def testReversr():
    p = url_for('blue.hehe')
    return p


@blue.route('/testArgs/')
def testArgs():
    name = request.args.get('name')
    print(name)
    name1 = request.args.getlist('name')
    print(name1)
    print(session)
    return 'testArgs'

@blue.route('/testForm/',methods=['post'])
def testForm():
    name = request.form.get('name')
    print(name)
    name1 = request.form.getlist('name')
    print(name1)
    return 'testArgs'

@blue.route('/response/')
def get_response():
    return '德玛西亚', 404

@blue.route('/rendertemplate/')
def render_temp():
    resp = render_template('welcomecookie.html')
    print(resp)
    print(type(resp))
    return resp,500

# @blue.route('/tologincookie/')
# def tologincookie():
#     return render_template('logincookie.html')
#
#
# @blue.route('/logincookie/',methods=['post'])
# def logincookie():
#     name = request.form.get('name')
#
#     response = redirect(url_for('blue.welcomecookie'))
#     response.set_cookie('name', name)
#
#     return response
#
# @blue.route('/welcomecookie/')
# def welcomecookie():
#     name = request.cookies.get('name', '游客')
#     return render_template('welcomecookie.html', name=name)
#
# @blue.route('/logoutcookie/')
# def logoutcookie():
#     response = redirect(url_for('blue.welcomecookie'))
#     response.delete_cookie('name')
#     return response

# session
@blue.route('/tologincookie/')
def tologincookie():
    return render_template('logincookie.html')


@blue.route('/logincookie/', methods=['post'])
def logincookie():
    name = request.form.get('name')

    session['name'] = name

    return redirect(url_for('blue.welcomecookie'))

@blue.route('/welcomecookie/')
def welcomecookie():
    name = session.get('name', '游客')
    return render_template('welcomecookie.html', name=name)

@blue.route('/logoutcookie/')
def logoutcookie():
    response = redirect(url_for('blue.welcomecookie'))
    response.delete_cookie('session')
    # session.pop('name')
    return response