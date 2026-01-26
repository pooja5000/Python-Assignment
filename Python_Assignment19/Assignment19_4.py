# 4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the 
# numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will 
# calculate its square. Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100] 
# Output of reduce = 204
from functools import reduce

filterx=lambda no: no%2==0
mapx=lambda no:no**2
reduceX=lambda no1,no2:no1+no2

def main():

    data=[]
    no=int(input("Enter no of elements:"))
    for i in range(no):
        elements=int(input())
        data.append(elements)

    print(data)
    
    res1=list(filter(filterx,data))
    print(res1)

    res2=list(map(mapx,res1))
    print(res2)

    res3=reduce(reduceX,res2)
    print(res3)

if __name__=="__main__":
    main()