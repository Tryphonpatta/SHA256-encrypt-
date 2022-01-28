import hashlib

class Block:
    def __init__(self, previous_block_hash):

        self.previous_block_hash = previous_block_hash

        self.block_data = previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

x = input()
init_block = Block(x)
print(init_block.block_data)
print(init_block.block_hash)
