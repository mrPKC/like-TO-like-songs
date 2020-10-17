from flask import Flask, render_template, redirect, request
from songs_popularity_based_recoomendation import predict
app = Flask(__name__)

#a = predict("In The End")

a = [['hi', 0]]


@app.route("/")
def hello():
    return render_template("index.html", len=len(a), a=a)


@app.route("/res", methods=["POST"])
def result():
    if request.method == "POST":
        # name = request.form["username"]
        no1 = str(request.form["num1"])
        a = predict(no1)
    # for i in a:
    #     return i
    return render_template("index.html", len=len(a), a=a)


app.run(use_reloader=True, debug=True)
