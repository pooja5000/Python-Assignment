# 5: Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
# Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronizatio

import threading

def dispaly():

    for i in range (1,50+1):
       print(i,end=" ")
            
def displayReverse():
    for i in range(50,0,-1):
        print(i,end=" ")

def main():
    
    t1=threading.Thread(target=dispaly)
    t1.start()
    t1.join()
    print("---------------------------------------------------------------------------------------------")
    t2=threading.Thread(target=displayReverse)
    t2.start()
    t2.join()

    

if __name__=="__main__":
    main()
        