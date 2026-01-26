# Write a program which accept number from user and return addition of digits in that number.
# Input: 5187934
# Output: 37

def display(no):
    sum=0
    while no>0:
        sum=sum+(no%10)
        no=no//10
        
    return sum

def main():
    no=int(input("Enter no:"))
    ret=display(no)
    print("No of digit in number:",ret)

if __name__=="__main__":
    main()