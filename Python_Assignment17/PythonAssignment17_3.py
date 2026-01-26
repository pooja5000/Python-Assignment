# Write a program which accept one number from user and return its factorial.
# Input: 5
# Output: 120

def fact(no):
    fact1=1
    for i in range (1,no+1):
        fact1=fact1*i
    return fact1
        

def main():
    no=int(input("Enter no:"))
    res=fact(no)
    print(res)

if __name__=="__main__":
    main()