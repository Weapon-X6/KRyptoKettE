from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from blockchain_utils import BlockChainUtils
from transaction import Transaction


class Wallet:
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    @staticmethod
    def is_signature_valid(data, signature, public_key_string):
        """Validates if a signature is valid."""
        signature = bytes.fromhex(signature)
        data_hash = BlockChainUtils.hash(data)
        publick_key = RSA.import_key(public_key_string)
        signature_scheme_object = PKCS1_v1_5.new(publick_key)
        is_valid = signature_scheme_object.verify(data_hash, signature)
        return is_valid

    def sign(self, data):
        """Takes some data and creates a signature."""
        dataHash = BlockChainUtils.hash(data)
        signature_scheme_object = PKCS1_v1_5.new(self.keyPair)
        signature = signature_scheme_object.sign(dataHash)

        return signature.hex()

    def public_key(self):
        return self.keyPair.public_key().export_key().decode()

    def create_transaction(self, receiver, amount, type):
        transaction = Transaction(self.public_key(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction
