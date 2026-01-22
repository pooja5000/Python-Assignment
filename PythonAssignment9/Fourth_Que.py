def cubeof(no):
   return no**3

def main():
    n=int(input("Enter number:"))
    ret=cubeof(n)
    print("Cube of",n,"is:",ret)

if __name__=="__main__":
    main()