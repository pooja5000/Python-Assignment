# 1: Design a Python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution

import threading

def even():

    for i in range(2,20+1,2):
        print(i)

def odd():

    for i in range(1,20,2):
        print(i)

def main():

    print("First 10 even numbers::")
    t1=threading.Thread(target=even())
    t1.start()

    print("First 10 even numbers::")
    t2=threading.Thread(target=odd)
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()
        