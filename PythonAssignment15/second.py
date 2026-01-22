#Write a lambda function using filter() which accepts a list of numbers and returns a list of even number

checkeven=lambda no:no%2==0

def main():
    data=[]

    print("Enter elements in list:")
    for i in range(5):
        no=int(input())
        data.append(no)
    print(data)

    result=list(filter(checkeven,data))
    print(result)
if __name__=="__main__":
    main()