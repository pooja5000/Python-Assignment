# Q5) Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not

def Seaech_Word(filename,word):

    
    fobj=open(filename,"r")
    data=fobj.read()
    print(data.split())

    words=data.split()
    count=0
    for i in words:
        if word==i:
            count=count+1
    
    if count>0:
        print("Found")

    else:
        print("Not found")
      

    
   
    

def main():

    filename=input("Enter the file:")
    word=input("Enter the word to be seach:")
    Seaech_Word(filename,word)

if __name__ =="__main__":
    main()