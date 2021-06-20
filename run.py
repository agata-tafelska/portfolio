from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/contact")
def contact():
    return render_template("gallery.html")


@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    if request.method == 'POST':
        return 'HTTP POST for user %s with password %s' % (username, request.form['password'])
    else:
        return 'HTTP GET for user %s' % username


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
