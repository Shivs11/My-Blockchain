import sys
import json

from flask.wrappers import Response
from flask import jsonify
from flask import request
from uuid import uuid4

from blockchain import BlockChain
from flask import Flask

sys.path.append(".")
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

my_blockchain = BlockChain()

@app.route('/mine', methods=['GET'])
def mine():
    #We have to now run the proof of algorithm to get the next proof:

    very_last_block = my_blockchain.last_block #Using our getter method defined via @property.
    very_last_proof = very_last_block['proof']
    current_proof = my_blockchain.proof_of_work(very_last_proof)

    #Since we have done the mining, we need an award, in the form of bitcoin, for finding the piece of proof:
    my_blockchain.add_transaction(
        sender="0",
        recipient=str(uuid4()).replace('-',''),
        amount = 1
    )

    #Now we have to forge the new block by adding it to the existing blockchain!
    previous_block_hash = my_blockchain.hash_function(very_last_block)
    added_block = my_blockchain.add_block(current_proof, previous_block_hash)

    response = {
        'message': "New Block Forged",
        'index': added_block['index'],
        'transactions': added_block['transactions'],
        'proof': added_block['proof'],
        'previous_hash': added_block['previous_hash'],
    }


    return jsonify(response), 200


@app.route('/transactions/new', methods = ['POST'])
def new_transactions():
    values = request.get_json()

    #To check if the response we have gotten fulfils our requirements:
    requirements = ['sender', 'recipient', 'amount']
    
    for item in values:
        if item not in requirements:
            return 'Missing values', 400


    #Time to create a new transaction:
    block_index = my_blockchain.add_transaction(values['sender'], values['recipient'], values['amount'])

    my_response = {'message': f'This transaction will be added to Block'}

    return jsonify(my_response), 201




@app.route('/chain', methods=['GET'])
def full_chain():
    my_response = {
        'chain': my_blockchain.chainer,
        'length': len(my_blockchain.chainer),
    }


    return jsonify(my_response) , 200

@app.route('/', methods=['GET'])
def tester():
    return "<h1> Your connection is testable and works as well </h1>"



@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')  #Getting a list of nodes (HTTP addresses) supplied.
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        my_blockchain.register_nodes(node)

    

    response ={
        'message': 'New nodes have been added',
        'total nodes': list(my_blockchain.nodes),
    }


    return jsonify(response), 201




if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

