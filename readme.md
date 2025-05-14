Command-Line Banking System
Overview
This is a simple command-line banking system built in Python, designed to practice core Python programming and Object-Oriented Programming (OOP) concepts. The system allows users to create bank accounts, check balances, deposit or withdraw money, and transfer funds between accounts. It features a secure password-based authentication mechanism and input validation to ensure robust functionality.
Features

Create Bank Accounts: Users can create accounts with a name, password, and initial deposit.
Check Balances: View account balance after verifying the password.
Deposit/Withdraw Money: Add or remove funds from an account, with validation for positive amounts and sufficient funds.
Transfer Funds: Transfer money between accounts, ensuring valid amounts and authentication.
Input Validation: Prevents negative deposits/withdrawals, insufficient funds, and incorrect passwords.
OOP Design: Utilizes classes (Bank and Account) with encapsulation (private attributes) and clear method responsibilities.

Technologies

Python: Version 3.6 or higher.
OOP Concepts: Classes, objects, encapsulation, and method-based operations.
Data Structure: Dictionary to store accounts in the Bank class.

Installation

Clone the Repository:git clone https://github.com/puritymasanya1/banking-system-simulation.git
cd banking-system


Ensure Python is Installed:
Verify Python 3.6+ is installed by running:python --version


If not installed, download it from python.org.


No External Dependencies:
The project uses only Python’s standard library, so no additional packages are required.



Usage

Run the Program:
Save the code in a file named banking_system.py.
Run the program using:python banking_system.py




Example Output:
The provided test code creates two accounts, performs deposits, withdrawals, balance checks, and transfers. Sample output:Masanya's account number: 1
Peter's account number: 2
Your new balance is £5400
Invalid deposit amount!
Amount must be greater than zero!
You have withdrawn £100.New balance is £3400
Your current balance is £5400.
Incorrect password!
You have transferred £300 to 2.New balance is £5100
Invalid input
Your current balance is £5100.
Incorrect password!




Interacting with the Code:
To extend the program, modify the if __name__ == "__main__": block to add more accounts or operations.
Example: Create a new account and check its balance:acc3_id = bank.create_account("Alice", "Pass333", 1000)
acc3 = bank.find_account(acc3_id)
print(acc3.check_balance("Pass333"))  # Output: Your current balance is £1000.





Code Structure

Classes:
Bank: Manages all accounts in a dictionary (self.accounts), with methods to create and find accounts.
Account: Represents an individual account, storing account number, name, password, and balance. Includes methods for deposit, withdrawal, balance checking, and transfers.


Key Methods:
Bank.create_account: Creates a new account with validation for positive initial deposits.
Bank.find_account: Retrieves an account by account number.
Account.deposit: Adds funds to the account balance.
Account.withdraw: Removes funds if sufficient balance exists.
Account.check_balance: Returns the balance if the password is correct.
Account.transfer: Transfers funds to another account after validation.


Encapsulation: Uses private attributes (__password, __balance) to protect sensitive data.

How It Works

Bank Initialization: The Bank class initializes an empty dictionary to store accounts.
Account Creation: The create_account method generates a unique account number, validates the initial deposit, creates an Account object, and stores it in the dictionary.
Account Operations:
Deposit/Withdrawal: Validates positive amounts and sufficient funds, updating the balance.
Balance Check: Requires correct password to display the balance.
Transfer: Verifies password, amount, and balance before transferring funds to another account.


Testing: The if __name__ == "__main__": block demonstrates all features with sample accounts and operations.

Future Improvements

Add a command-line interface (CLI) for interactive user input.
Implement password hashing (e.g., using hashlib) for enhanced security.
Add transaction history to track deposits, withdrawals, and transfers.
Support multiple currencies or interest calculations.
Integrate a database (e.g., SQLite) for persistent storage.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make changes and commit (git commit -m "Add feature").
Push to your branch (git push origin feature-branch).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions or feedback, reach out via GitHub Issues or contact your-email@example.com.
