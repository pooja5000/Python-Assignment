# Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

from math import sqrt

def primeno(no):

    if no<=1:
        return False
    for i in range(2,int(sqrt(no))+1):
        if no%i==0:
            return False
    return True
    
def main():
    n=int(input("Enter number to be check:"))
    ret=primeno(n)

    if ret==True:
        print("Prime")
    else:
        print("Not prime")
if __name__=="__main__":
    main()