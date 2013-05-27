from flask import Flask, url_for, session, escape, request, redirect ,render_template
app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s <p> <a href="/logout"> logout</a>' %escape(session['username'])
    return 'You are not logged in <p> <a href="/login"> go to login</a>'

@app.route('/student/<username>/')
def student(username):
    return 'Hello %s' % username

@app.route('/method' , methods=['GET','POST'])
def test_HTTP_method():
    if request.method == 'POST':
        return request.method
    else:
        return request.method + '<p>' + request.args.get('name') + '<p>' + request.args.get('password')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method  == "POST":
        name    = request.form['name']
        passwd  = request.form['password']
        if name:
            session['username']=name
        return redirect(url_for('hello'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/loginpage')
def hello():
    return render_template('loginpage.html',name=session['username'])

    


if __name__ == '__main__':
	app.debug = True
        app.secret_key = '\xf7^\xf6!\xd8)47\xa5\xda\x04\xf2\xdejU\x99_"]\xa9\x886\x0b\xe5'
	app.run()