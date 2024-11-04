import pprint

from block import Block
from transaction import Transaction
from transaction_pool import TransactionPool
from wallet import Wallet

if __name__ == "__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    transaction_type = "TRANSFER"

    wallet = Wallet()
    fraudulent_wallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.create_transaction(receiver, amount, transaction_type)

    if pool.is_transaction_new(transaction):
        pool.add_transaction(transaction)

    # block = Block(pool.transactions, "last_hash_placholder", "forger_placeholder", 1)
    block = wallet.create_block(pool.transactions, "last_hash", 1)
    pprint.pprint(block.to_json())
    is_signature_valid = wallet.is_signature_valid(
        block.payload(), block.signature, fraudulent_wallet.public_key()
    )
    print(is_signature_valid)
