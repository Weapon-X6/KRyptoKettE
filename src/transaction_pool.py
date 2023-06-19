class TransactionPool:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def is_transaction_new(self, transaction):
        for t in self.transactions:
            if t == transaction:
                return False
        return True
