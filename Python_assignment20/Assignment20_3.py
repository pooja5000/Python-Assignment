# 3.Design a Python application that creates two threads named EvenList and OddList.
# Both threads should accept a list of integers as input.
# The EvenList thread should:
# Extract all even elements from the list.
# Calculate and display their sum.
# The OddList thread should:
# Extract all odd elements from the list.
# Calculate and display their sum.
# Threads should run concurrently.

import threading

def eventhread(items):
    sum=0
    for i in range(len(items)):

        if items[i]%2==0:
            print("even numbers::",items[i])
            sum=sum+items[i]
    print("Sum of even:",sum)
            
            
def odd(items):
    sum=0
    for i in range(len(items)):
        if items[i]%2!=0:
            print("Odd numbers::",items[i])
            sum=sum+items[i]
    print("Sum of odd:",sum)
    

def main():
    no=int(input("Enter no of elements::"))
    data=[]
    print("Enter elements in list")

    for i in range(no):
        elements=int(input())
        data.append(elements)
    print(data)

    t1=threading.Thread(target=eventhread,args=(data,))
    t1.start()
    
    t2=threading.Thread(target=odd,args=(data,))
    t2.start()

    t1.join()
    t2.join()

    print("Exist from main")

if __name__=="__main__":
    main()
        