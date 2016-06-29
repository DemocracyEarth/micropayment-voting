#!/usr/bin/env python3
from flask import Flask, jsonify, request, abort
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# set up bitrequest client for BitTransfer requests
wallet = Wallet()
requests = BitTransferRequests(wallet)

# server address
server_url = 'http://localhost:8000/'


# Service
app = Flask(__name__)

# /wallet route to verify our wallet
@app.route('/wallet', methods=['GET'])
def get_wallet():
	return jsonify({'wallet': wallet.get_payout_address()})


# /send-vote route to submit a vote
@app.route('/send-vote', methods=['POST'])
def sendvote():
	if not request.json or not 'voters_id' in request.json:
		abort(400)
	voters_id = request.json['voters_id']
	proposal = request.json['proposal']
	vote = {
	  'id': voters_id,
	  'proposal': proposal,
	  'submitted_to': play(voters_id),
	  'done': True
	}
	return jsonify(vote)

def play(voter_id_from_web):
    ans = str(voter_id_from_web)
    sel_url = server_url + 'write-vote?id={0}'
    answer = requests.get(url=sel_url.format(ans))
    return answer.text

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8008)
