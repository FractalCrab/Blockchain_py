from block import Block

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.all_transactions=[]
        self.genesis_block()

    def genesis_block(self):
        transactions={}
        previous_hash=0
        self.chain.append(Block(transactions,previous_hash))
        return self.chain


    def print_blocks(self):
          for i in range(len(self.chain)):
              current_block = self.chain[i]
              print("Block {} {}".format(i, current_block))
              current_block.print_contents()
    #add block
    def add_block(self,transactions):
        previous_block_hash=self.chain[len(self.chain)-1].hash
        new_block=Block(transactions,previous_block_hash)
        self.chain.append(new_block)

    """for checking and validatign chain"""
    def check_chain(self):

      for i in range(1, len(self.chain)):
          current = self.chain[i]
          previous = self.chain[i-1]
      if(current.hash != current.generate_hash()):
        print("Current hash of the block is not equal to the generated hash of the block.")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("The previous block's hash is not equal to the previous hash value stored in the current block.")
        return False
      return True
