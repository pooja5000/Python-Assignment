# Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 2 3 4 6 12

def factors(no):
    item=list()
    for i in range(1,no+1):
        if no%i==0:
            item.append(i)
    return item

def main():
    n=int(input("Enter number:"))
    ret=factors(n)
    print(ret)

if __name__=="__main__":
    main()
