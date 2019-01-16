#!use/bin/ Python3
#coding:utf-8

from flask import Flask,url_for, request,render_template
# from requests import Request


app=Flask(__name__)

@app.route("/")
def hello_world():
    print(request.method)
    return "happyboy welcome"

@app.route("/helloword")
def hello_liuqiang():
    return "liuqiang"

@app.route("/hello/<username>")
def priuntUserName(username=None):

    return render_template("index.html",username=username)

@app.route("/post")
def post():
    return "helloword111 "

with app.test_request_context():
    url_for("hello_world",method='POST')
    url_for("priuntUserName",username="xiaoliu")
    url_for("hello_world",next="/")

@app.route("/init",methods=["GET","POST"])
def getInit():

    if request.method == 'GET':
        return "1111"
    else:
        return "22222"


if __name__ =="__main__":
    app.debug=True
    app.run()





