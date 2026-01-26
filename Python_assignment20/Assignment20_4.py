# 4: Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
# Thread ID
# 0 Thread Name

import threading

def small(str1):
    print("Small==")
    count=0
    for i in str1:
        if i.islower():
            print(i,end= "")
            count=count+1

    print("Id of thread:",threading.current_thread().name,"is:", threading.get_ident())

    

def Capital(str1):
    count=0
    print()
    print("Capital==")
    for i in str1:
        if i.isupper():
            print(i, end="") 
            count=count+1 
    print("Id of thread:",threading.current_thread().name,"is:", threading.get_ident())
             

def Digits(str1):
    print()
    print("Numbers==:")
    count=0
    for i in str1:
        if i.isdigit():
            print(i,end="")
            count=count+1

    print("Id of thread:",threading.current_thread().name,"is:", threading.get_ident())
            
 
    

def main():
    word=input("Enter the string::")


    t1=threading.Thread(target=small,args=(word,))
    t1.start()
    t1.join()
    
    t2=threading.Thread(target=Capital,args=(word,))
    t2.start()
    t2.join()

    t3=threading.Thread(target=Digits,args=(word,))
    t3.start()
    t3.join()
    
    print()
    print("Exist from main")
    print("Id of thread:",threading.current_thread().name,"is:", threading.get_ident())

if __name__=="__main__":
    main()
        