
# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.
from functools import reduce


def main():

    data=[]
    print("Enter no's")

    for i in range(5):
        no=int(input())
        data.append(no)
    print(data)
    result=reduce((lambda no1,no2:no1 if no1>no2 else no2),data)

    print("largest no is:",result)

if __name__=="__main__":
    main()