from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    publicKey = request.form['publicKey']
    secretKey = request.form['secretKey']
    airtime = request.form['airtime']
    amount = request.form['amount']
    number = request.form['number']

    return (request.form['airtime'])

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
	app.run()
