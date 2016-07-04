#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# set up bitrequest client for BitTransfer requests
wallet = Wallet()
requests = BitTransferRequests(wallet)

# server address
server_url = 'http://localhost:8000/'


# Start flask service
app = Flask(__name__)

# definition of micropayment_sendvote function
def micropayment_sendvote(proposal):
	'''
	Function: micropayment_sendvote()

	Arguments:
	 -	proposal: sting.
	 	Possible values: yes / no
	'''
    ans = str(proposal)
    sel_url = server_url + 'write-vote?proposal={0}'
    answer = requests.post(url=sel_url.format(ans))
    return answer.text


# /wallet route to verify our wallet
@app.route('/wallet', methods=['GET'])
def get_wallet():
	return jsonify({'wallet': wallet.get_payout_address()})


# /send-vote route to submit a vote
@app.route('/send-vote', methods=['POST'])
def sendvote():
	if not request.json or not 'proposal' in request.json:
		abort(400)
	proposal = request.json['proposal']
	vote = {
	  'proposal': proposal,
	  'submitted_to': micropayment_sendvote(proposal),
	  'done': True
	}
	return jsonify(vote)

# /vote-count
@app.route('/vote-count', methods=['GET'])
def grabvotes():
	sel_url = server_url + 'count'
	total_votes = requests.get(url=sel_url.format())
	return jsonify(total_votes.text)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8008)
