#!/usr/bin/env python3
import logging

from flask import Flask
from flask import request

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet('./proposal.json')
payment = Payment(app, wallet)

@app.route('/write-vote')
@payment.required(1)
def writevote():
	# extract answer from client request
	answer = request.args.get('id')
	voted_id = "Vote OK: " + answer + " to wallet: " + wallet.get_payout_address()
	logging.info(voted_id)
	print(voted_id)
	return wallet.get_payout_address()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
