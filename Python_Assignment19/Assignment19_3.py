# 3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted 
# from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
# Map function will increase each number by 10. Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 
# List after filter = [76, 89, 86, 90, 70] 
# List after map = [86, 99, 96, 100, 80] 
# Output of reduce = 6538752000
from functools import reduce

filterx=lambda no: no>=70 and no<=90
mapx=lambda no:no+10
reduceX=lambda no1,no2:no1*no2

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