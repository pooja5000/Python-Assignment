# 5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of 
# numbers. List contains 
# the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will 
# multiply each number by 2. Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).
# Input List = [2, 70, 11, 10, 17, 23, 31, 77] 
# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 62] 
# Output of reduce = 62
from functools import reduce
from math import sqrt

def chkprime(no):
    if no<=1:
        return False
    for i in range(2,int(sqrt(no))+1):
        if no%i==0:
            return False
    return True

mapx=lambda no:no*2

def max(no1,no2):
    if no1>no2:
        no2=no1
    return no2

def main():

    data=[]
    no=int(input("Enter no of elements:"))
    for i in range(no):
        elements=int(input())
        data.append(elements)

    print(data)
    
    res1=list(filter(chkprime,data))
    print(res1)

    res2=list(map(mapx,res1))
    print(res2)

    res3=reduce(max,res2)
    print(res3)

if __name__=="__main__":
    main()