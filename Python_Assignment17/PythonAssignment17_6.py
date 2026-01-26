# Write a program which accept one number and display below pattern.
# Input: 5
# Output:
# *****
# ****
# ***
# **
# *

def display(no):

    for i in range(no+1,0,-1):
        print(" ")
        for j in range(0,i):
            print("*",end=" ")
            

def main():
    no=int(input("Enter no:"))
    display(no)

if __name__=="__main__":
    main()