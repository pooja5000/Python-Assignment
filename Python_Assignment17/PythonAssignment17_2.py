# Write a program which accept one number and display below pattern.
# Input: 5
# Output:* * * * *
#        * * * * *
#        * * * * *
#        * * * * *
#        * * * * *

def display():

    for i in range (5):
        print(" ")
        for j in range(5):
            print("*",end=" ")
        

def main():

    display()
    

if __name__=="__main__":
    main()