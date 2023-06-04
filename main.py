from flask import Flask, request, redirect, render_template, url_for
from replit import db
app = Flask(__name__, static_url_path="/static")

@app.route("/signup", methods=["POST"])
def createUser():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect("/login")
  else:
    return redirect("/signup")

@app.route("/login", methods=["POST"])
def doLogin():
  keys = db.keys()
  form = request.form
  if form["username"] not in keys:
    return "Credentials not recognized"
  else:
    if form["password"]==db[form["username"]]["password"]:
      return redirect('/home')
    else:
      return redirect("/login")



@app.route("/login")
def login():
  page = ""
  f = open("templates/login.html", "r")
  page = f.read()
  f.close()

  css_url = url_for("static", filename="signup.css")
  page = page + '<link rel="stylesheet" href="{}">'.format(css_url)
  return page


@app.route("/signup")
def signup():
  page = ""
  f = open("templates/signup.html", "r")
  page = f.read()
  f.close()

  css_url = url_for("static", filename="signup.css")
  page = page + '<link rel="stylesheet" href="{}">'.format(css_url)
  return page

@app.route('/')
def index():
    return render_template ("welcome.html", css_url=url_for("static", filename="signup.css"))

@app.route('/intro')
def intro():
    return render_template ("intro.html", css_url=url_for("static", filename="signup.css"))

@app.route('/home')
def home():
    return render_template("home.html", css_url=url_for("static", filename="signup.css"))

app.run(host='0.0.0.0', port=81)
