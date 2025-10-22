class BankAccount:
    def __init__(self, acc_number, name):
        self.number = acc_number
        self.acc_name = name
        self.bank_balance = 0

    def deposit(self, amount):
        self.bank_balance = amount + self.bank_balance
        print(self.bank_balance)

    def withdraw(self, amount_1):
        self.bank_balance = self.bank_balance - amount_1
        print(self.bank_balance)

    def get_balance(self):
        print(self.bank_balance)


customer_1 = BankAccount(1, "sarthak")
print(customer_1.number)
print(customer_1.bank_balance)
customer_1.deposit(100)
customer_1.withdraw(60)
customer_1.get_balance()