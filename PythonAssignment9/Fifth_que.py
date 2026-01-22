# Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15
# Output: Divisible by 3 and 5

def Divisibleby(no):
    if no%3==0 and no%5==0:
        return True
    else:
        return False

def main():

    n=int(input("Enter number :"))
    ret=Divisibleby(n)

    if ret==True:
        print("Number is divisible by 3 or 5")
    else:
        print("Number is not divisible by 3 or 5")

if __name__=="__main__":
    main()