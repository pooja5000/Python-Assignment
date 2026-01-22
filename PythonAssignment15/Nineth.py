#Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.
from functools import reduce
def main():

    n=int(input("Enter no f elements you want..."))
    data=[]
    print("Enter elements:")
    for i in range (n):
        no=int(input())
        data.append(no)

    print(data)

    result=reduce(lambda no1,no2:no1*no2,data)
    print(result)

if __name__=="__main__":
    main()