from flask import Flask, render_template, redirect, url_for, abort, make_response
from flask import request
import os

from markupsafe import escape

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['extra-value'] = 'simple example'
    return resp


print(os.getlogin())


@app.route("/me")
def me_api():
    user = os.getlogin()
    return {
        "username": user,
        "theme": 'dark'
    }


#
# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]


if __name__ == '__main__':
    app.debug = True
    app.run()
