#Write a lambda function using filter() which accepts a list of numbers and returns a list of even number
checkodd=lambda no:no%2!=0

def main():
    data=[]
    print("Enter no's:")

    for i in range(5):
        no=int(input())
        data.append(no)
    print(data)

    result=list(filter(checkodd,data))
    print(result)


if __name__=="__main__":
    main()