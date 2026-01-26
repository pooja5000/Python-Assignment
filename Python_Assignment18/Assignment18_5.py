# Write a program which accept N numbers from user and store it into List. Return addition of all prime 
# numbers from that List. Main python file accepts N numbers from user and pass each number to 
# ChkPrime() function which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().
# Input: Number of elements: 11
# Input Elements: 13 5 45 7 4 56 10 34 2 5 8
# Output: 54 (13+5+7+2+5)
from marvellous import ChkPrime

def Chk_list(items):
    sum=0
    
    for i in range(len(items)):
        if ChkPrime(items[i])==True:
            sum=sum+items[i]
    return sum

def main():
    no=int(input("Enter number:"))

    data=[]
    print("Enter elements")
    for i in range(no):
        elements=int(input())
        data.append(elements)
    res=Chk_list(data)
    print("Sum of prime no is:",res)
     
    # if ChkPrime(no)==False:
    #     print("prime")
    # else:
    #     print("No")




    
        

if __name__=="__main__":
    main()
    