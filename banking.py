from abc import ABCMeta, abstractmethod
from random import randint

# Abstract Class defining a blueprint for the Account functionality
class Account(metaclass=ABCMeta):

    # Abstract method to create a new account
    @abstractmethod
    def createAccount():
        return 0

    # Abstract method to authenticate an existing account
    @abstractmethod
    def authenticate():
        return 0

    # Abstract method to withdraw money from the account
    @abstractmethod
    def withdraw():
        return 0

    # Abstract method to deposit money into the account
    @abstractmethod
    def deposit():
        return 0

    # Abstract method to display the balance of the account
    @abstractmethod
    def displayBalance():
        return 0


# SavingsAccount class implementing the Account interface
class SavingsAccount(Account):
    def __init__(self):
        # Dictionary to store account information
        # Key: Account Number, Value: [Account Holder's Name, Balance]
        self.savingsAccounts = {}

    # Method to create a new savings account
    def createAccount(self, name, initialDeposit):
        print()
        # Generate a random 5-digit account number
        self.accountNumber = randint(10000, 99999)
        # Store the new account with name and initial deposit
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account creation has been successful. Your account number is ", self.accountNumber)
        print()

    # Method to authenticate an account using account holder's name and account number
    def authenticate(self, name, accountNumber):
        print()
        # Check if the account number exists in the dictionary
        if accountNumber in self.savingsAccounts.keys():
            # Check if the name matches with the stored name for the given account number
            if self.savingsAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                # Set the current account number for future transactions
                self.accountNumber = accountNumber
                print()
                return True
            else:
                print("Authentication Failed: Name does not match.")
                print()
                return False
        else:
            print("Authentication Failed: Account number not found.")
            print()
            return False

    # Method to withdraw money from the authenticated account
    def withdraw(self, withdrawalAmount):
        print()
        # Check if the withdrawal amount exceeds the available balance
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            # Deduct the withdrawal amount from the current balance
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was successful.")
            # Display the updated balance after withdrawal
            self.displayBalance()
        print()

    # Method to deposit money into the authenticated account
    def deposit(self, depositAmount):
        print()
        # Add the deposit amount to the current balance
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was successful.")
        # Display the updated balance after deposit
        self.displayBalance()
        print()

    # Method to display the current balance of the authenticated account
    def displayBalance(self):
        print("Available balance: ", self.savingsAccounts[self.accountNumber][1])


# Instantiate the SavingsAccount class
savingsAccount = SavingsAccount()

# Main loop for the user interface
while True:
    print()
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")

    # Get user input for the desired action
    userChoice = int(input())
    print()

    # Option 1: Create a new account
    if userChoice == 1:
        print()
        # Get the user's name and initial deposit for the new account
        name = input("Enter your name: ")
        deposit = int(input("Enter the initial deposit: "))
        # Create the account
        savingsAccount.createAccount(name, deposit)
        print()

    # Option 2: Access an existing account
    elif userChoice == 2:
        print()
        # Get the user's name and account number for authentication
        name = input("Enter your name: ")
        accountNumber = int(input("Enter your account number: "))
        # Authenticate the account
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        print()

        # If authentication is successful, provide further options
        if authenticationStatus:
            while True:
                print()
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous menu")
                # Get user input for further operations
                userChoice = int(input())
                print()

                # Option 1: Withdraw money
                if userChoice == 1:
                    print()
                    withdrawalAmount = int(input("Enter a withdrawal amount: "))
                    savingsAccount.withdraw(withdrawalAmount)
                    print()

                # Option 2: Deposit money
                elif userChoice == 2:
                    print()
                    depositAmount = int(input("Enter an amount to be deposited: "))
                    savingsAccount.deposit(depositAmount)
                    print()

                # Option 3: Display balance
                elif userChoice == 3:
                    print()
                    savingsAccount.displayBalance()
                    print()

                # Option 4: Go back to the main menu
                elif userChoice == 4:
                    break

    # Option 3: Exit the program
    elif userChoice == 3:
        quit()
