from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        if "about" in request.form:
            return redirect(url_for("about"))
        elif "projects" in request.form:
            return redirect(url_for("projects"))
        elif "blog" in request.form:
            return redirect(url_for("blog"))
        elif "donation" in request.form:
            return redirect(url_for("donation"))
    else:
        return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/donation")
def donation():
    return render_template("donation.html")


if __name__ == "__main__":
    app.run()
