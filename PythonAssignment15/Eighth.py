# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

def main():

    data=[]
    print("Enter no's")

    for i in range(5):
        no=int(input())
        data.append(no)
    print(data)
    result=list(filter(lambda no:no%5==0 and no%3==0,data))

    print("No divisible by3 and 5 is:",result)

if __name__=="__main__":
    main()
