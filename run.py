from flask import Flask
from flask import render_template
from flask import request
from AzureDB import AzureDB

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template("contact_success.html", email=request.form['email'])
    else:
        return render_template("contact.html")


@app.route("/guests", methods=['GET', 'POST'])
def guests():
    if request.method == 'POST':
        database = AzureDB()
        database.insert_note(name=request.form['name'], text=request.form['text'])
        notes = database.get_notes()
        for note in notes:
            print("%s wrote :\"%s\"" % (note[0], note[1]))
        return render_template("guests.html", notes=notes)
    else:
        database = AzureDB()
        notes = database.get_notes()
        return render_template("guests.html", notes=notes)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
