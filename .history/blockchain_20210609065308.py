import hashlib
import json

from time import time
from uuid import uuid4


class BlockChain(my_object):
    def __init__(self) -> None:
        self.chainer = []  # Having a chain implemented as a list.
        self.present_transactions = [] # Having a list to keep track of current transactions
    

    def add_transaction(self, sender, recipient, amount):
        #This is used to add a transaction to our list of transactions.
        self.present_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })


        return self.last_block['index'] + 1
    

    def add_block(self):
        #Creates a new block and adds it to our "Blockchain"
        pass

    def proof_of_work(self, previous_proof):
        #This function will be developed to find a number p such that a hash value of (pp') contains 4 leading
        #zeroes. Here, p' is the number in the previous iteration.

        my_proof = 0
        while self.valid_proof is False:
            my_proof += 1
        

        return proof


    #Adding a static method to our class:
    @staticmethod
    def hash_function(my_block):
        # Have to create a SHA256 hash of a block:

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


    
