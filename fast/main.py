from flask import Flask,render_template
from flask_login import login_required

app = Flask(__name__)


@app.route('/')
def  bean():
    return render_template('home.html')

@app.route('/login')
def  login():
    return render_template('login.html')
    
    
@app.route('/signup')
def  signup():
    return render_template('signup.html')

if  __name__ == '__main__':
    app.run(debug = True)
