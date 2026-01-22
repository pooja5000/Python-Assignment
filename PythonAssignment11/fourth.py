# Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def RevOfDigit(no):
    rev=0
    while(no>0):
        digit=no%10
        rev=(rev*10)+digit
        no=no//10
    return rev
    
def main():
    n=int(input("Enter the number::"))
    ret=RevOfDigit(n)
    print(ret)


if __name__=="__main__":
    main()