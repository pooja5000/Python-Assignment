# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
#Input: 10 20
#Output: 20 is greater

def ChkGreater(No1,No2):
    if No1>No2:
        return No1
    else:
        return No2

def main():
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    ret=ChkGreater(n1,n2)
    print("Greater number is:",ret)

if __name__=="__main__":
    main()
