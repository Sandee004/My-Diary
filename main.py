from flask import Flask, render_template, request, session, flash, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        password = request.form["password"]
        session["user"] = user
        session["password"] = password
        flash('Signup successful')
        return render_template('homepage.html')
    else:
        if "user" in session:
            flash("User already exists. Login")
            return redirect(url_for('login'))
        return render_template('register.html')
    

@app.route('/login/', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        password = request.form.get("Password")
        if password and password == session.get("password"):
            flash('Welcome')
            return render_template('homepage.html')
        else:
            return 'Wrong password'
    return render_template('login.html')
    


@app.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("password", None)
    flash('Logout successful')
    return redirect(url_for('register'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
