# 3: Write a Python program to implement a class named Arithmetic with the following characteristics:
# The class should contain two instance variables: Valuel and Value2.
# Define a constructor (init) that initializes all instance variables to 0.
# Implement the following instance methods:
# Accept() accepts values for Valuel and Value2 from the user.
# Addition() - returns the addition of Valuel and Value2.
# Subtraction() returns the subtraction of Valuel and Value2.
# Multiplication() returns the multiplication of Valuel and Value2.
# Division() returns the division of Valuel and Value2 (handle division by zero properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods

class Arithmetic:
    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter first value:"))
        self.Value2=int(input("Enter second value:"))

    def Addition(self):
        return self.Value1+self.Value2
    
    def Subtraction(self):
        return self.Value1-self.Value2
    
    def multiplication(self):
        return self.Value1*self.Value2
    def division(self):
        try:
            return self.Value1/self.Value2
        except ZeroDivisionError:
            print("Unable to devide by 0")

    
a1=Arithmetic()
a1.Accept()
print("Addition is:",a1.Addition())
print("Subtraction is:",a1.Subtraction())
print("multiplication is:",a1.multiplication())
print("division is:",a1.division())

a2=Arithmetic()
a2.Accept()
print("Addition is:",a2.Addition())
print("Subtraction is:",a2.Subtraction())
print("multiplication is:",a2.multiplication())
print("division is:",a2.division())

a3=Arithmetic()
a3.Accept()
print("Addition is:",a3.Addition())
print("Subtraction is:",a3.Subtraction())
print("multiplication is:",a3.multiplication())
print("division is:",a3.division())