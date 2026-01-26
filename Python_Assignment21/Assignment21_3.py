
# 3: Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.
import threading
count=0
lobj=threading.Lock()
def increment():
    global count

    for i in range(200):
        with lobj:
           count=count+1



def main():
    global count
    t1=threading.Thread(target=increment)
    t1.start()
    

    t2=threading.Thread(target=increment)
    t2.start()
    t1.join()
    t2.join()
    print(count)

if __name__=="__main__":
    main()