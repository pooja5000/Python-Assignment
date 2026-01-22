# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

def main():

    data=[]
    print("Enter no's")

    for i in range(5):
        str1=(input())
        data.append(str1)
    print(data)
    result=list(filter(lambda str1:len(str1)>5,data))

    print("Size more than 5 is:",result)

if __name__=="__main__":
    main()
