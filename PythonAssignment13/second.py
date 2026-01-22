#Write a program which accepts radius of circle and prints area of circle.

def areaofcircle(radius):
    return 3.14*(radius*radius)

def main():
    r=int(input("Enter radius:"))
    ret=areaofcircle(r)
    print("Area of circle::",ret)

if __name__=="__main__":
    main()