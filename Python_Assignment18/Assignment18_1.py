# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input: Number of elements: 6
# Input Elements: 13 45 7 4 56
# Output: 130

def summation(no):
    
    sum=0
    for i in len(no):
        sum=sum+no[i]
    return sum
def main():
    no=int(input("Enter number:"))
    data=[]
    print("Enter items into list:")
    for i in range(no):
        elements=int(input())
        data.append(elements)
    print(data)
    ret=summation(data)
    print("Summation is:",ret)
        

if __name__=="__main__":
    main()
    