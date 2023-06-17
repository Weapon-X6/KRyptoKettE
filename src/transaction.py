import time
import uuid


class Transaction:

    def __init__(self, senderPublicKey, receiverPublicKey, amount, transactionType):
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.amount = amount
        self.transactionType = transactionType
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__
    
    def sign(self, signature):
        self.signature = signature