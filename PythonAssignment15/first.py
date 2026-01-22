# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

square=lambda no:no*no

def main():
    data=[]
    print("Enter elements in list:")
    for i in range(5):
        no=int(input())
        data.append(no)
    print(data)

    result=list(map(square,data))
    print(result)

if __name__=="__main__":
    main()