from transaction import Transaction


if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1 
    transactionType  = 'TRANSFER'
    transaction = Transaction(sender, receiver, amount, transactionType)
    print(transaction.toJson())
