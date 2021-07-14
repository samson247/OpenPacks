from flask import Flask
from flask import render_template
from openPacks import getCards, getPack
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/openPack')
def openPack():
	#data = getCards()
	data = getPack()
	return render_template('main.html', filenames=data)