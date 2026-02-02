# Q2) Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt

def Count_Word(filename):

    fobj=open(filename,"r")
    
    data=fobj.read()

    word=data.split()

    print("no of words:",len(word))

def main():

    filename=input("Enter the file name:")
    Count_Word(filename)

if __name__ =="__main__":
    main()