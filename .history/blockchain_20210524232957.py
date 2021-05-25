class BlockChain(my_object):
    def __init__(self) -> None:
        self.chainer = []  # Having a chain implemented as a list.
        self.present_transactions = [] # Having a list to keep track of current transactions
    

    def add_transaction(self):
        #This is used to add a transaction to our list of transactions.
        pass
    

    def add_block(self):
        #Creates a new block and adds it to our "Blockchain"
        pass


    #Adding a static method to our class:
    @staticmethod
    def hash_function(my_block):
        pass

    @property
    def last_block(self):
        #Return the last block in the blockchain
        pass


    
