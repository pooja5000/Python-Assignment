# 1: Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.
import threading
import math

def chkprime(item):
    if item<=1:
        return False
    for i in range(2,int(math.sqrt(item))+1):
        if item%i==0:
            return False
    return True

def prime(items):
    prime1=[]
    for i in items:
        if chkprime(i):
            prime1.append(i)

    print(prime1)

def nonprime(items):
    prime1=[]
    
    for i in items:
        if chkprime(i)==False:
            prime1.append(i)

    print(prime1)

def main():

    data=[]
    print("Enter elements:")
    for i in range(6):
        elements=int(input())
        data.append(elements)

    print(data)

    t1=threading.Thread(target=prime,args=[data,])
    t1.start()
    t1.join()

    t2=threading.Thread(target=nonprime,args=[data,])
    t2.start()
    t2.join()

if __name__=="__main__":
    main()

            


