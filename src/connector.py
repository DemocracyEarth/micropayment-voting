#!/usr/bin/env python3
import logging

from flask import Flask
from flask import request
from flask import jsonify

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

proposal_yes = 0
proposal_no = 0

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)



def increase_proposal(value):
	global proposal_yes, proposal_no
	if value == 'yes':
		proposal_yes = proposal_yes + 1
	elif value == 'no':
		proposal_no = proposal_no + 1
	else:
		print('Value for proposal is not valid')


@app.route('/write-vote', methods=['POST'])
@payment.required(1)
def writevote():
	# extract answer from client request
	proposal_value = request.args.get('proposal')
	increase_proposal(str(proposal_value))
	return wallet.get_payout_address()

@app.route('/count')
@payment.required(1)
def status():
	global proposal_yes, proposal_no
	count = 'yes: ' + str(proposal_yes) + ', no: ' + str(proposal_no)
	return count

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
