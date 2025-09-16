from flask import Flask, render_template, redirect, url_for
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route("/")
@app.route("/anasayfa")
def home():
    return render_template("index.html")

@app.route("/tedaviler")
def treatment():
    return render_template("treatment.html")

@app.route("/tedaviler/<tedavi>")
def treatment_detail(tedavi):
    try:
        return render_template(f"treatments/{tedavi}.html")
    except TemplateNotFound:
        return redirect(url_for("home"))

@app.route("/galeri")
def gallery():
    return render_template("gallery.html")

@app.route("/hakkimizda")
def about():
    return render_template("about.html")

@app.route("/iletisim")
def contact():
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=False)
