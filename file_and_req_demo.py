from flask import Flask, render_template, redirect, url_for, abort, make_response
from flask import request
import os

from markupsafe import escape

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# root route
@app.route("/")
def home():
    return " <h1> This is homepage of File demo </h1>"


# file to show route
@app.route("/file")
@app.route("/file/<name>")
def file(name=None):
    return render_template('index.html', name=name)


# uploading file route
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'the_file' not in request.files:
            return 'No file part'

        file_uploaded = request.files['the_file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file_uploaded.filename == '':
            return 'No selected file'

        if file_uploaded:
            # Save the file to the project directory
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_uploaded.filename)
            file_uploaded.save(file_path)
            return 'File uploaded successfully'

    # If the request method is GET, just display the upload form
    return render_template("upload_file.html")


# request object route
@app.route('/req', methods=['POST', 'GET'])
def get_request():
    # .get() is used to when the filed is optional, we can add default value if not given
    search_word = request.args.get('key', 'default_key')
    print(search_word)
    if request.method == 'POST':
        return request.form['username']


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/redirect/<url>')
def redirect_page(url):
    return redirect(url_for(escape(url)))


@app.route('/get_error')
def get_error():
    abort(401)


#   print("error")


if __name__ == '__main__':
    app.debug = True
    app.run()
