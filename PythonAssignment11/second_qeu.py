# 2.Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def CountOfDigit(no):
    count=0
    while(no>0):
        count=count+1
        no=no//10
    return count


def main():
    n=int(input("Enter the number::"))
    print(n%10)
    ret=CountOfDigit(n)
    print(ret)


if __name__=="__main__":
    main()