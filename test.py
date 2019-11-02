from blockchain import Blockchain

new_transactions = [{'patient':"test",
'disease':"heart attack",
'medication':'aspirin'}]


my_blockchain = Blockchain()
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()
my_blockchain.chain[1].transactions = 'fake'
my_blockchain.check_chain()
