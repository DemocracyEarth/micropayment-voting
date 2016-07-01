# API Endpoints


Web browser <--> Front-end <--> **api.py <--> connector.py**

## api.py
RESTful service for vote saving. This module only receives and transmits
information to the connector.py script and to the front-end instances.

Resource | HTTP Method | URL and arguments | Returns
----|-----|----- |-----|
Vote saving | POST | <host:port>/send-vote?proposal=yes/no | JSON object with confirmation, vote and the wallet's address that stores our votes
Vote status | GET | <host:port>/vote-count | Total number of votes on each option for the proposal



## connector.py
21.co server for operations over micropayments (One satoshi per operation). This
connector provides information for the api.py module and manages the operations
for Blockchain events

Resource | HTTP Method | URL and arguments | Returns
----|-----|-----|-----|
Vote accounting to the Blockchain | POST |  <host:port>/write-vote?proposal=yes/no | Wallet address
Votes on each proposal | GET | <host:port>/count | Total votes for the proposal
