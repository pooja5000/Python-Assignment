# Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
# Input: 11
# 5
# Output: 16

def add(No1,No2):
    return No1+No2

def main():
    
    No1=int(input("Enter 1st no:"))
    No2=int(input("Enter 2nd no:"))
    res=add(No1,No2)
    print("Addition is:",res)

if __name__=="__main__":
    main()

