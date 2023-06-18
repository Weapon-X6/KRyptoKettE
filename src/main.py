from transaction import Transaction
from wallet import Wallet

if __name__ == "__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    transaction_type = "TRANSFER"

    wallet = Wallet()
    transaction = wallet.create_transaction(receiver, amount, transaction_type)
    print(transaction.payload())
    is_signature_valid = Wallet.is_signature_valid(
        transaction.payload(), transaction.signature, Wallet().public_key()
    )
    print(f"Is valid? {is_signature_valid}")
