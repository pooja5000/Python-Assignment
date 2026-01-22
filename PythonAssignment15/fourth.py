from functools import reduce

summation=lambda no1,no2:no1+no2

def main():

    data=[]
    print("Enter no's")

    for i in range(5):
        no=int(input())
        data.append(no)
    print(data)
    result=reduce(summation,data)

    print("Addition is:",result)

if __name__=="__main__":
    main()