'''Importing datetime library for recording timestamp'''
from datetime import datetime

from hashlib import sha256

#creating a block for blockhchain

class Block:
    def __init__(self,transactions,previous_hash,nonce=0):
        self.transactions=transactions
        self.previous_hash=previous_hash
        self.nonce=nonce
        self.timestamp=datetime.now()
    #generating hash for the block
    def generate_hash(self):
        block_details=str(self.timestamp)+str(self.transcations)+str(self.previous_hash)+str(self.nonce)
        block_hash=sha256(block_details.encode())
        return block_hash.hexdigest()
