# Savings Account Management System

A simple console-based savings account management system that allows users to create new accounts, authenticate existing accounts, and perform basic banking operations such as withdrawals, deposits, and balance inquiries.

## Features

- **Create Account**: Users can create a new savings account by providing their name and an initial deposit. A random account number is generated.
- **Authenticate Account**: Users can log into their existing accounts by providing their name and account number.
- **Withdraw Funds**: Users can withdraw money from their account if they have sufficient balance.
- **Deposit Funds**: Users can deposit money into their account.
- **Check Balance**: Users can check the available balance in their account.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/shivangmedhekar/Simple-Banking-Program-in-Python.git
    cd Simple-Banking-Program-in-Python
    ```

2. Ensure Python is installed (Python 3.x is recommended). You can check the version with:

    ```bash
    python --version
    ```

3. Run the script:

    ```bash
    python banking.py
    ```

## How to Use

1. **Create a New Account**: Choose option `1` to create a new account, then enter your name and initial deposit.
2. **Access an Existing Account**: Choose option `2`, then enter your name and account number to authenticate.
   - Once authenticated, you can:
     - Withdraw money
     - Deposit money
     - Check your account balance
3. **Exit the Program**: Choose option `3` to exit.

### Example Usage

```
Enter 1 to create a new account
Enter 2 to access an existing account
Enter 3 to exit

1
Enter your name: John Doe
Enter the initial deposit: 5000
Account creation has been successful. Your account number is 12345

Enter 1 to create a new account
Enter 2 to access an existing account
Enter 3 to exit

2
Enter your name: John Doe
Enter your account number: 12345
Authentication Successful

Enter 1 to withdraw
Enter 2 to deposit
Enter 3 to display available balance
Enter 4 to go back to the previous menu

3
Available balance: 5000
```

## Classes & Methods

### **Account (Abstract Class)**
Defines the interface for basic account operations:
- `createAccount()`
- `authenticate()`
- `withdraw()`
- `deposit()`
- `displayBalance()`

### **SavingsAccount (Subclass)**
Implements the methods from the `Account` class and includes account management functionalities.

- `createAccount(name, initialDeposit)`: Creates a new account with a random account number.
- `authenticate(name, accountNumber)`: Authenticates the user based on the provided name and account number.
- `withdraw(withdrawalAmount)`: Withdraws funds if the account has sufficient balance.
- `deposit(depositAmount)`: Deposits money into the user's account.
- `displayBalance()`: Displays the current balance of the authenticated account.

## Future Enhancements

- Add interest calculation for savings accounts.
- Implement transaction logs to track withdrawals and deposits.
- Add stronger authentication mechanisms (e.g., passwords or PINs).
- Enable fund transfers between accounts.

## Developer

|  **Shivang Medhekar** |
| :---: |
| [![Shivang Medhekar](https://avatars2.githubusercontent.com/u/69140290?s=200&u=5df35a82b6d2b6b7b876dfdc22d451c92d30a5c6&v=4)](https://github.com/shivangmedhekar) | 
| <a href="https://github.com/shivangmedhekar" target="_blank">`github.com/shivangmedhekar`</a>|
  
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

