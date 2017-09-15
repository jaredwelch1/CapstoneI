from flask import Flask, render_template, session, request
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
Bootstrap(app)

app.secret_key = os.urandom(12) 


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
        return render_template('about.html')

@app.route('/test')
def test_route():
  return render_template('test.html')

if __name__ == '__main__':
	
	app.run(debug=True)
