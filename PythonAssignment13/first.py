#Write a program which accepts length and width of rectangle and prints area.

def areaofrect(length,width):
    return length*width

def main():
    l=int(input("Enter height:"))
    w=int(input("Enter width:"))
    ret=areaofrect(l,w)
    print("Area of rectangle::",ret)

if __name__=="__main__":
    main()
