# Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 5 4 3 2 1


def main():
    n=int(input("Enter no of elements:"))
    
    for i in range(n,0,-1):
        print(i)

if __name__=="__main__":
    main()
