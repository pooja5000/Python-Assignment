# Q1) Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo.txt.

def Count_Line(filename):

    fobj=open(filename,"r")
    #print(len(fobj.readlines())) 1st option
    lines=sum(1 for _ in fobj)

    print("no of lines:",lines)

def main():

    filename=input("Enter the file name:")
    Count_Line(filename)

if __name__ =="__main__":
    main()