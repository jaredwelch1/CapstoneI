from flask import Flask, render_template, session, request

import os

app = Flask(__name__)

app.secret_key = os.urandom(12) 


@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/test')
def test_route():
  return render_template('test.html')

if __name__ == '__main__':
	
	app.run(debug=True)
