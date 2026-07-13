class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")

    def withdrawAmount(self, withdraw):
        if withdraw > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= withdraw
            print(f"Balance after withdraw: {self.balance}")


name = input("Enter account holder name: ")
balance = int(input("Enter current balance: "))

bank = BankAccount(name, balance)

amount = int(input("Enter deposit amount: "))
bank.deposit(amount)

withdraw = int(input("Enter withdraw amount: "))
bank.withdrawAmount(withdraw)