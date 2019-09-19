

from flask import Blueprint, render_template, request, url_for, session


from werkzeug.utils import redirect

blue = Blueprint('blue', __name__)
@blue.route('/')
def hello_world():
    return 'hello'

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