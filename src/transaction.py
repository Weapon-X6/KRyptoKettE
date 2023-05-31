import uuid
import time

class Transaction():

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