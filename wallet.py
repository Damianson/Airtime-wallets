from flask import Flask, render_template
from flask import request
import requests
import json

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

    url = 'https://api.wallets.africa/bills/airtime/purchase'
    headers = {'Authorization': 'Bearer ' + publicKey}
    payload = {'Code': str(airtime),
               'Amount': int(amount),
               'PhoneNumber': str(number),
               'SecretKey': str(secretKey)}
    r = requests.post(url, headers=headers, json=payload)
    feedback = r.json()
    code_back = feedback['ResponseCode']
    message = feedback['Message']
    
    if code_back == 100:
        return render_template('success.html', message=message)
    else:
        return render_template('fail.html', message=message)

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
	app.run(debug=True)
