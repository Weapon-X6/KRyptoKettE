import json

from Crypto.Hash import SHA256


class BlockChainUtils:        
    @staticmethod
    def hash(data):
        data_string = json.dumps(data)
        data_bytes = data_string.encode('utf-8')
        data_hash = SHA256.new(data_bytes)
        return data_hash