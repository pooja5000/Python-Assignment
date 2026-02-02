# Q5) Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt


import os
import sys

def CheckFile(file1,word):

    fobj=open(file1,"r")

    data=fobj.read()

    print(data.count(word))

    fobj.close()
    

def main():
    if len(sys.argv)!=3:
        print("Invalid no of arguments")
        return
    CheckFile(sys.argv[1],sys.argv[2])
    
      
 
if __name__=="__main__":
    main()