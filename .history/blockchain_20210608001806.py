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

        


    #Adding a static method to our class:
    @staticmethod
    def hash_function(my_block):
        # Have to create a SHA256 hash of a block:

        pass

    @property
    def last_block(self):
        #Return the last block in the blockchain
        return self.chainer[-1]


    
