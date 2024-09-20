class Account:
    accounts = []

    def __init__(self, account_number, owner, balance):
        # __Private attributes
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance
        Account.accounts.append(self)
        #It refers to static list belonging to the Account class.Adds the created account object to the static accounts list.

    def deposit(self, amount):
        if amount > 0:
            
            self.__balance += amount
            print(f"{amount} has been deposited to account {self.__account_number}. New balance: {self.__balance:.2f}")
            Bank.track_transaction(f"{amount} was deposited to account {self.__account_number}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"{amount} withdrawn. Current balance: {self.__balance}")
                Bank.track_transaction(f"{amount} was withdrawn from account {self.__account_number}.")
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    def view_balance(self):
        print(f"Account Owner: {self.__owner}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance:.2f}")

class Bank:
    transactionHistory = []
    
    @staticmethod
    def displayBankInfo():
        print("Bank Name: Python Bank")
        print("Total Number of Accounts:", len(Account.accounts))
        print("Total Number of Transactions:", len(Bank.transactionHistory))

    @staticmethod
    def track_transaction(description):
        Bank.transactionHistory.append(description)

    @staticmethod
    def display_transaction_history():
        print("\nTransaction History:")
        for transaction in Bank.transactionHistory:
            print(transaction)

acc1 = Account("123456", "Alice", 1000.0)
acc1.view_balance()
acc1.deposit(500)
acc1.withdraw(200)
acc1.view_balance()

Bank.displayBankInfo()
Bank.display_transaction_history()
