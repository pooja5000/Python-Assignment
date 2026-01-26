# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
# Input: Number of elements: 4
# Input Elements: 13 5 45 7
# Output: 5

def Minimum(items):
    
    smallest=items[0]
    for i in range(len(items)):
        if smallest>items[i]:
            smallest=items[i]
    return smallest

def main():
    no=int(input("Enter number:"))
    data=[]
    print("Enter items into list:")
    for i in range(no):
        elements=int(input())
        data.append(elements)
    print(data)
    ret=Minimum(data)
    print("Smallest no is:",ret)
        

if __name__=="__main__":
    main()
    