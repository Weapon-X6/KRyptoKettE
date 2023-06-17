from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from blockchain_utils import BlockChainUtils


class Wallet:

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        """Takes some data and creates a signature"""
        dataHash = BlockChainUtils.hash(data)
        signatureSchemaObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemaObject.sign(dataHash)

        return signature.hex()