class Transaction:
    def __init__(self, date, type, amount, balance):
        self.date = date
        self.type = type
        self.amount = amount
        self.balance = balance
        self.next = None

class BankAccount:
    def __init__(self):
        self.head = None

    def add_transaction(self, date, type, amount, balance):
        transaction = Transaction(date, type, amount, balance)
        transaction.next = self.head
        self.head = transaction
    def display_transactions(self):
        transaction = self.head
        while transaction:
            print(transaction.date, transaction.type, transaction.amount, transaction.balance)
            transaction = transaction.next

account = BankAccount()
account.add_transaction("2023-01-01", "Deposit", 1000, 1000)
account.add_transaction("2023-01-02", "Withdrawal", 500, 500)
account.add_transaction("2023-01-03", "Deposit", 100, 600)
account.display_transactions()
