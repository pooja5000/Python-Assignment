# Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
# Input: Number of elements: 11
# Input Elements: 13 5 45 7 4 56 5 34 2 5 65
# Element to search: 5
# Output: 3

def frequency(items,no):
    
    count=0
    for i in range(len(items)):
        if no==items[i]:
            count=count+1
    return count

def main():
    no=int(input("Enter number:"))
    data=[]
    print("Enter items into list:")
    for i in range(no):
        elements=int(input())
        data.append(elements)
    print(data)
    n=int(input("Enter no to be check of its occurance is list:"))
    ret=frequency(data,n)
    print("Frequency no is:",ret)
        

if __name__=="__main__":
    main()
    