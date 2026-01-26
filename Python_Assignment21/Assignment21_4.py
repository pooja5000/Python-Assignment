
# 4: Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading


def summatiomn(items,result):
    sum1=0
    for i in items:
        sum1=sum1+i
    result["Add"]= sum1

def multiplication(items,result):
    product=1
    for i in items:
        product=product*i
    result["product"]=product



def main():

    result={}
    no=int(input("Enter no of elements to be enter"))
    data=[]
    for i in range(no):
        element=int(input())
        data.append(element)

    print(data)

    t1=threading.Thread(target=summatiomn,args=(data,result,))
    t1.start()
    t2=threading.Thread(target=multiplication,args=(data,result,))
    t2.start()
    t1.join()
    t2.join()

    print("Sum is:",result["Add"])
    print("Product is:",result["product"])
    

if __name__=="__main__":
    main()