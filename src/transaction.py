import copy
import time
import uuid


class Transaction:
    def __init__(
        self, sender_public_key, receiver_public_key, amount, transaction_type
    ):
        self.sender_public_key = sender_public_key
        self.receiver_public_key = receiver_public_key
        self.amount = amount
        self.transaction_type = transaction_type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ""

    def to_json(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature

    def payload(self):
        transaction_json = copy.deepcopy(self.to_json())
        transaction_json["signature"] = ""
        return transaction_json
