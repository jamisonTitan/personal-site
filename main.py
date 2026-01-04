from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        #determine what button was pressed from the main page
        #by querying the request object sent from the POST req
        #and render the appropriate html from static/templates
        match list(request.form.to_dict().keys())[0]:
            case "about":
                return redirect(url_for("about"))
            case "projects":
                return redirect(url_for("projects"))
            case "blog":
                return redirect(url_for("blog"))
            case "donation":
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
