# Write a lambda function which accepts one number and returns square of that number.

square=lambda no:no*no

def main():
    no=int(input("Enter no:"))
    print(square(no))

if __name__=="__main__":
    main()