from fileinput import filename

from flask import Flask, url_for, make_response, render_template
from markupsafe import escape
from flask import request

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'WELCOME TO FLASK'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def show_user(username):
    return f'User {escape(username)}'


# here we can use int, string, float path, uuid in string
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post you entered {post_id}'


@app.route('/path/<path:path>')
def sub_path(path):
    return f'{escape(path)}'


# auto converts slash in end if not given by request
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/method', methods=['GET', 'POST'])
def get_method():
    if request.method == 'POST':
        return "This is post req"
    else:
        return "This is get req"


@app.route("/hello")
def hello():
    return "Hello is called"


@app.route("/file")
def file():
    return render_template('index.html', name=None)


# this to test in console context your api
with app.test_request_context('/hello', method='POST'):
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user', username='John Doe'))
    assert request.path == '/hello'
    assert request.method == 'POST'
    # print(url_for('templates', filename='index.html'))

if __name__ == '__main__':
    app.debug = True
    app.run()
