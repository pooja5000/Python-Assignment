# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input: Number of elements: 7
# Input Elements: 13 5 45 7 4 56 34
# Output: 56

def Maximum(items):
    
    largest=0
    for i in range(len(items)):
        if items[i]>largest:
            largest=items[i]
    return largest

def main():
    no=int(input("Enter number:"))
    data=[]
    print("Enter items into list:")
    for i in range(no):
        elements=int(input())
        data.append(elements)
    print(data)
    ret=Maximum(data)
    print("Largest no is:",ret)
        

if __name__=="__main__":
    main()
    