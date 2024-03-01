class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

account = BankAccount(1000)
print(account.get_balance()) # 1000
account.deposit(500)
print(account.get_balance()) # 1500
account.withdraw(2000) # Insufficient funds
print(account.get_balance()) # 1500
