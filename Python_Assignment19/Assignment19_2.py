# Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4 3
# Output : 12
# Input : 6 3
# Output : 18

mul=lambda no1,no2:no1*no2

def main():

    no1=int(input("Enter fisrt number:"))
    no2=int(input("Enter second number:"))

    print("Multiplication is :",mul(no1,no2))

if __name__=="__main__":
    main()