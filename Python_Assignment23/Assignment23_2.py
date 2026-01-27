# 2: Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)
# The class should contain one class variable:
# ROI (Rate of Interest), initialized to 10.5
# Define a constructor (_init ) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display() displays account holder name and current balance
# Deposit()- accepts an amount from the user and adds it to balance
# Withdraw() accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest() calculates and returns interest using formula: Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI=10.5

    def __init__(self):
        self.Name="Pooja"
        self.Amount=1000

    def display(self):
        print("Account holder:",self.Name)
        print("Current balance:",self.Amount)

        
    def deposit(self):
        self.deposit=int(input("Enter ammount to be deposit:"))
        print("Current balance after deposit ammount:",self.Amount+self.deposit)
        self.Amount=self.deposit+self.Amount

    def withdraw(self):
        self.withdraw=int(input("Enter amount to be withdraw:"))
        if self.Amount>self.withdraw:
            print("Current balance after deposit ammount:",self.Amount-self.withdraw)
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        self.interest=(self.Amount*BankAccount.ROI)/100
        print("Intrest is:",self.interest)
        print("------------------------------------------------------------")

b1=BankAccount()
b1.display()
b1.deposit()
b1.withdraw()
b1.CalculateInterest()

b2=BankAccount()
b2.display()
b2.deposit()
b2.withdraw()
b2.CalculateInterest()


        