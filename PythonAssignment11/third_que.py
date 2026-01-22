# Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def SumOfDigit(no):
    sum=0
    while(no>0):
        sum=sum+no%10
        no=no//10
    return sum


def main():
    n=int(input("Enter the number::"))
    ret=SumOfDigit(n)
    print(ret)


if __name__=="__main__":
    main()