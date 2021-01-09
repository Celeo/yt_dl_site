from subprocess import call
from threading import Thread
from typing import Union

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)
from werkzeug.wrappers import Response


app = Flask(__name__)
app.config.from_json("config.json")


@app.route("/")
def index() -> Union[Response, str]:
    if "auth" in session:
        return redirect(url_for("save"))
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login() -> Response:
    given = request.form.get("password")
    if "auth" in session:
        del session["auth"]
    if not given:
        flash("Password not supplied", "error")
        return redirect(url_for("index"))
    if given == app.config["LOGIN_PASSWORD"]:
        flash("Logged in", "success")
        session["auth"] = True
    else:
        flash("Invalid password", "error")
    return redirect(url_for("save"))


@app.route("/save", methods=["GET", "POST"])
def save() -> Union[Response, str]:
    if "auth" not in session:
        return redirect(url_for("index"))
    if request.method == "GET":
        return render_template("save.html")
    url = request.form.get("url")
    if not url:
        flash("URL no supplied", "error")
        return redirect(url_for("save"))
    flash("Download started", "success")
    Thread(target=download, args=(url,)).start()
    return redirect(url_for("save"))


def download(url: str) -> None:
    call(["youtube-dl", url])


if __name__ == "__main__":
    app.run(port=5000, debug=True)
