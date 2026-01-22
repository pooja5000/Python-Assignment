# Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

def perfect(no):
    sum=0
    for i in range(1,no):
        if no%i==0:
            sum=sum+i
    return sum

def main():

    n=int(input("Enter no:"))
    ret=perfect(n)
    if ret==n:
        print("Perfect!!!")
    else:
        print("Not Perfect!!!")

if __name__=="__main__":
    main()
