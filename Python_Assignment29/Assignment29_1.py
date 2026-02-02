# Q1) Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not.
import os
import sys

def CheckFile(filename):
    ret=os.path.exists(filename)

    if (ret==True):
        print("File is exist:")

    else:
        print("File is not exist")

def main():
    filename=input("Enter file name:")
    CheckFile(filename)
    
    
 
if __name__=="__main__":
    main()