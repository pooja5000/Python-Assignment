# Write a program which accept one number for user and check whether number is prime or not.
# Input: 5
# Output: It is Prime Number
from math import sqrt

def main():

    
    no=int(input("Enter no:"))
    if no<=0 and no==1:
        print("No")
    for i in range (2,int(sqrt(no))+1):
        if no%i==0:
            print("No")
            return
        
    print("Yes")
    

if __name__=="__main__":
    main()