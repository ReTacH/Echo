from flask import Flask, render_template, request
# from .app import insert_message, random_messages

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")
    # if request.method == 'GET':
    #     return render_template("submit.html")
    # else:
    #     insert_message(request)
    #     return render_template("submit.html", thanks = True)

@app.route("/more/")
def more():
    # msg = random_messages(5)
    return render_template("more.html")

@app.route("/method/")
def method():
    return render_template("method.html")
