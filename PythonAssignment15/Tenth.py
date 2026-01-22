#Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

# Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.
from functools import reduce


def main():

    data=[]
    print("Enter no's")

    for i in range(5):
        no=int(input())
        data.append(no)
    print(data)
    result=list(filter((lambda no:no%2==0),data))

    print("Count of even:",len(result))

if __name__=="__main__":
    main()

