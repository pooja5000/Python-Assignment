# Write a program which accepts one number and prints all even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10
def chkeven(no):
    items=list()
    for i in range(1,no+1):
        if i%2==0:
            items.append(i)
    return items

def main():
    n=int(input("Enter number:"))
    ret=chkeven(n)  
    print(ret)        
if __name__=="__main__":
    main()
