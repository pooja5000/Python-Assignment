# Write a program which accept number from user and return number of digits in that number.
# Input: 5187934
# Output: 7

def display(no):
    count=0
    while no>0:
        no=no//10
        count=count+1
        
    return count

def main():
    no=int(input("Enter no:"))
    ret=display(no)
    print("No of digit in number:",ret)

if __name__=="__main__":
    main()