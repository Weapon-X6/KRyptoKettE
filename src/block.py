import copy
import time


class Block:
    def __init__(self, transactions, last_hash, forger, block_count):
        self.transactions = transactions
        self.last_hash = last_hash
        self.forger = forger
        self.block_count = block_count
        self.timestamp = time.time()
        self.signature = ""

    def to_json(self):
        data = {}
        data["transactions"] = [tr.to_json() for tr in self.transactions]
        data["last_hash"] = self.last_hash
        data["forger"] = self.forger
        data["block_count"] = self.block_count
        data["timestamp"] = self.timestamp
        data["signature"] = self.signature

        return data

    def payload(self):
        json_repr = copy.deepcopy(self.to_json())
        json_repr["signature"] = ""
        return json_repr

    def sign(self, signature):
        self.signature = signature
