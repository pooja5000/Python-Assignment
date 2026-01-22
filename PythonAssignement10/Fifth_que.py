#Write a program which accepts one number and prints all odd numbers till that number.

def chkodd(no):
    items=list()
    for i in range(1,no+1):
        if i%2!=0:
            items.append(i)
    return items

def main():
    n=int(input("Enter no:"))
    ret=chkodd(n)

    print(ret)

if __name__=="__main__":
    main()