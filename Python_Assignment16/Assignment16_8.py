# Write a program which accept number from user and print that number of "*" on screen.
# Input: 5
# Output:* * * * *


def main():
    
    no=int(input("Enter number:"))
    for i in range(no):
        print("*",end=" ")

if __name__=="__main__":
    main()

