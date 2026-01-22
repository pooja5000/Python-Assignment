#Write a program which accepts one number and prints square of that number.
def squareof(no):
    return no**2

def main():
    n=int(input("Enter number:"))
    ret=squareof(n)
    print("Square of number:",ret)

if __name__=="__main__":
    main()
