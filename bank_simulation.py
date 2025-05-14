'''
Build a simple command-line banking system where users can:
1. Create bank accounts
2. Check balances
3. Deposit/Withdraw money
4. Transfer funds
All while practicing core Python and OOP concepts.
'''


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self, name, password, initial_deposit):
        if initial_deposit < 0:
            print("Deposit must be greater than zero!")
            return None  # Handles invalid account creation
       
        acc_number = len(self.accounts) + 1  # Ensures each account has a unique number
        new_account = Account(acc_number, name, password, initial_deposit)  # Initializes a new account with user input
        self.accounts[acc_number] = new_account  # Adds the new account to the bank's account dictionary
        return acc_number  # Return the ID so thr caller can reference the account later
          
    def find_account(self, acc_number):
        if acc_number in self.accounts:
            return self.accounts[acc_number]
        else:
            return None


class Account:
    def __init__(self, acc_number, name, password, balance=0):
        self.acc_number = acc_number
        self.name = name
        self.__password = password
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount!"
        self.__balance += amount
        return f"Your new balance is £{self.__balance}"     

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be greater than zero!"
        if amount > self.__balance:
            return "Insufficient funds."
        self.__balance -= amount
        return f"You have withdrawn £{amount}.New balance is £{self.__balance}"

    def check_balance(self, password):
        if password != self.__password:
            return "Incorrect password!"
        else:
            return f"Your current balance is £{self.__balance}."

    def transfer(self, target_account, amount, password):
        if password != self.__password:
            return "Incorrect password!"
        if amount <= 0:
            return "Invalid input"
        if amount > self.__balance:
            return "Insufficient funds!"
        self.__balance -= amount
        target_account.deposit(amount)
        return f"You have transferred £{amount} to {target_account.acc_number}.New balance is £{self.__balance}"

# Test the code
# Create a bank instance and add accounts


if __name__ == "__main__":
    bank = Bank()

    acc1_id = bank.create_account("Masanya", "Pass111", 5000)
    acc2_id = bank.create_account("Peter", "Pass222", 3500)

    print(f"Masanya's account number: {acc1_id}")
    print(f"Peter's account number: {acc2_id}")

    acc1 = bank.find_account(acc1_id)
    acc2 = bank.find_account(acc2_id)

    # Test deposit
    print(acc1.deposit(400)) 
    print(acc2.deposit(-100))

    # Test withdraw
    print(acc1.withdraw(-1000))
    print(acc2.withdraw(100))

    # Test check balance
    print(acc1.check_balance("Pass111"))
    print(acc1.check_balance("Pess222"))

    # Test transfer
    print(acc1.transfer(acc2, 300, "Pass111"))
    print(acc2.transfer(acc1, -300, "Pass222"))

    # Test Check balance
    print(acc1.check_balance("Pass111"))
    print(acc2.check_balance("Pass11"))
