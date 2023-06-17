from transaction import Transaction
from wallet import Wallet

if __name__ == "__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    transactionType = "TRANSFER"

    transaction = Transaction(sender, receiver, amount, transactionType)

    wallet = Wallet()
    signature = wallet.sign(transaction.to_json())
    transaction.sign(signature)

    is_signature_valid = Wallet.is_signature_valid(
        transaction.payload(), signature, wallet.public_key()
    )
    print(f"Is valid? {is_signature_valid}")
