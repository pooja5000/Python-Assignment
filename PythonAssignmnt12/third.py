def add(no1,no2):
     return no1+no2
   

def sub(no1,no2):
     return no1-no2


def div(no1,no2):
     return no1/no2

def mul(no1,no2):
    return no1*no2
    

def main():
    n1=int(input("Enter number 1:"))
    n2=int(input("Enter number 2:"))
    ret=add(n1,n2)
    print("Addition is :",ret)
    ret=sub(n1,n2)
    print("Subtraction is :",ret)
    ret=mul(n1,n2)
    print("Multiplication :",ret)
    ret=div(n1,n2)
    print("Division is :",ret)

if __name__=="__main__":
    main()
