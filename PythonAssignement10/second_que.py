def summation(no):
    sum=0
    for i in range(1,no+1):
        sum=sum+i
    return sum


def main():
    n=int(input("Enter no of elements:"))
    ret=summation(n)
    print("Addition is :",ret)

if __name__=="__main__":
    main()