# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should:
# Identify all even factors of the given number.
# 0 Calculate and display the sum of even factors.
# The OddFactor thread should:
# Identify all odd factors of the given number.
# Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message: "Exit from main"

import threading

def evenfactor(no):
    sum=0
    for i in range(2,no,2):
        
        if no%i==0:
            print(i)
            sum=sum+i
    print("Sum of even:",sum)
            
            
def odd(no):
    sum=0
    for i in range(1,no,2):
        
        if no%i==0:
            print(i)
            sum=sum+i
    print("Sum of odd:",sum)
    

def main():

    print("First 10 even numbers::")
    t1=threading.Thread(target=evenfactor,args=(12,))
    t1.start()
    t1.join()

    print("First 10 odd numbers::")
    t2=threading.Thread(target=odd,args=(12,))
    t2.start()
    t2.join()

    print("Exist from main")

if __name__=="__main__":
    main()
        