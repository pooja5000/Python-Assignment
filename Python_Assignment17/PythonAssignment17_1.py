# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() 
# for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
from Arithmetic import *

def main():

    no1=int(input("Enter first number:"))
    no2=int(input("Enter second number:"))

    addition=Add(no1,no2)
    print("Addition is:",addition)

    Subtraction=Sub(no1,no2)
    print("Subtraction is:",Subtraction)

    Multiplication=Mul(no1,no2)
    print("Multiplication is:",Multiplication)

    Division=Div(no1,no2)
    print(Division)

if __name__=="__main__":
    main()