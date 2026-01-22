#Write a program which accepts marks and displays grade.
def grade(marks):
    
    if marks>=75:
        return "Distinction"
    
    elif marks>=60:
        return "First class"
    
    elif marks>=50:
        return "Second class"
    
    else:
        return "Fail"
    
def main():
     marks=int(input("Enter Marks:"))
     ret=grade(marks)
     print(ret)

if __name__=="__main__":
        main()