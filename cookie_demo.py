from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/cookies')
def cookies():
    # Create a response object
    resp = make_response('Setting a cookie!')

    # Set a cookie named 'example_cookie' with value 'example_value'
    resp.set_cookie('status', 'true')
    return resp


@app.route('/get_cookie')
def get_cookie():
    # Access the value of the cookie named 'example_cookie'
    cookie_value = request.cookies.get('status')
    if cookie_value:
        return f'The value of the cookie is: {cookie_value}'
    else:
        return 'Cookie not found.'


@app.route('/')
def index():
    return "WELCOME TO FLASK"


@app.route('/delete_cookie')
def delete_cookie():
    # Create a response object
    resp = make_response('Cookie deleted!')

    # Set the 'example_cookie' with an expiration date in the past (to delete it)
    resp.set_cookie('status', expires=0)

    return resp


if __name__ == '__main__':
    app.run(debug=True)
