# Write a program which accept one number and display below pattern.
# Input: 5
# Output:
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def display(no):

    for i in range(1,no+1):
        print()
          
        for j in range(1,no+1):
            print(j,end=" ")
            
            

def main():
    no=int(input("Enter no:"))
    display(no)

if __name__=="__main__":
    main()