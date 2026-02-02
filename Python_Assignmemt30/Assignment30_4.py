# Q4) Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# First file is an existing file
# Second file is a new file
# Copy all contents from the first file into the second file.
# Input:
# ABC.txt Demo.txt
# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

def Count_Line(filename1,filename2):

    fobj1=open(filename1,"w")
    fobj2=open(filename2,"r")
    data=fobj2.read()
    fobj1.write(data)

def main():

    filename1=input("Enter the new file:")
    filename2=input("Enter the existing file:")
    Count_Line(filename1,filename2)
    print("Data successfully copied into new file")

if __name__ =="__main__":
    main()