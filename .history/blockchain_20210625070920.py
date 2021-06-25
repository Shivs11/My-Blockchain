import hashlib
import json

from time import time
from uuid import uuid4
from urllib.parse import urlparse
import requests
#NOTES:
#Each block in our entire blockchain has the following:
# 1. An index, a timestamp, a list of transactions defining it, a proof and the hash of the previous block.
#


class BlockChain(object):
    def __init__(self) -> None:
        self.nodes = set() #Declaring a set of nodes in hopes of making the entire system decentralized.

        self.chainer = []  # Having a chain implemented as a list.
        self.present_transactions = [] # Having a list to keep track of current transactions

        #Creating the very first block, also called the genesis block, of our blockchain:
        self.add_block(previous_hash = 1, proof = 100)

    def add_transaction(self, sender, recipient, amount):
        #This is used to add a transaction to our list of transactions in the same block
        self.present_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        #returns the index of the block which the transaction will be added to—the next one to be mined. 

        return self.last_block['index'] + 1

    def valid_chain(self, chainer):
        first_block = chainer[0]
        next_index = 1

        while(next_index < len(chainer)):
            current_block = chainer[next_index]
    

    def register_nodes(self, address):
        self.nodes.add(urlparse(address).netloc)

    def add_block(self, proof, previous_hash = None):
        #Creates a new Block in our blockchain:

        create_block = {
            'index': len(self.chainer) + 1,
            'timestamp': time(),
            'transactions': self.present_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash_function(self.chainer[-1])
        }

        self.chainer.append(create_block)

        #Now, we clear the list of the current transactions:
        self.present_transactions = []

        return create_block

    def proof_of_work(self, previous_proof):
        #This function will be developed to find a number p such that a hash value of (pp') contains 4 leading
        #zeroes. Here, p' is the number in the previous iteration.

        my_proof = 0
        while self.valid_proof(previous_proof, my_proof) is False:
            my_proof += 1
        

        return my_proof


    #Adding a static method to our class:
    @staticmethod
    def hash_function(my_block):
        # Takes in a block of a blockchain and calculates the SHA-256 hash for that block:

        pass


    @staticmethod
    def valid_proof(last_proof, proof):
        #This function is meant to validate our proof concept by performing the computation of hash(last_proof, proof) 
        #in order to evaluate if the answer evaluates to having 0 leading zeros or not.

        #We first convert the parameters given to us into bytes:
        bytes_converted = f'{last_proof}{proof}'.encode()
        hash_value = hashlib.sha256(bytes_converted).hexdigest()

        return hash_value[:4] == "0000"

    @property
    def last_block(self):
        #Return the last block in the blockchain
        return self.chainer[-1]


    
