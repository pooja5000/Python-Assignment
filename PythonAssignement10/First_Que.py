#Write a program which accepts one number and prints multiplication table of that number.
# Input: 4
# Output:
# 4 8 12 16 20 24 28 32 36 40

def table(no):
    items=list()
    for i in range(1,11):
        items.append(i*no)
    return items

def main():
    
    n=int(input("Enter no:"))
    ret=table(n)
    print(ret)

if __name__=="__main__":
    main()