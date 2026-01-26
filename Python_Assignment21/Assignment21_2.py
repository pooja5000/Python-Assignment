# 2: Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.
import threading
def max(items):
    large=0
    for i in items:
        if i>large:
            large=i
    print("largest no is:",large)
    

def min(items):
    small=items[0]
    for i in items:
        if i<small:
            small=i
            
    print("Smallest no is:",small)

def main():
    no=int(input("Enter no of elements:"))
    data=[]
    print("Enter elements:")
    for i in range(no):
        elements=int(input())
        data.append(elements)
    print(data)

    t1=threading.Thread(target=max,args=(data,))
    t1.start()
    t1.join()

    t2=threading.Thread(target=min,args=(data,))
    t2.start()
    t2.join()

if __name__=="__main__":
    main()