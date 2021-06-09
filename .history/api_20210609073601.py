import sys

from flask.wrappers import Response
sys.path.append(".")

from blockchain import BlockChain
from flask import Flask


app = Flask(__name__)

my_blockchain = BlockChain()

@app.route('/mine', methods=['GET'])
def mine():
    return "This will be mining a new block in our blockchain"


@app.route('/transactions/new', methods = ['POST'])
def new_transactions():
    return "We shall be adding a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    my_response = {
        'chain': my_blockchain.chain,
        'length': len(my_blockchain.chain),
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

