# 3: Write a Python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:
# Value
# Define a constructor (init) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# ChkPrime() returns True if the number is prime, otherwise returns False
# ChkPerfect() returns True if the number is perfect, otherwise returns False
# 0 Factors()- displays all factors of the number
# SumFactors() returns the sum of all factors
# (You may use this method as a helper in ChkPerfect() if required)
# Create multiple objects and call all methods
from math import sqrt
class Number:
    def __init__(self):
        
        self.value=int(input("Enter the number:"))

    def ChkPrime(self): 
        if self.value<1:
            return False
        for i in range(2,int(sqrt(self.value))+1):
            if self.value%i==0:
                return False

        return True
            
    def ChkPerfect(self):
        sum1=0
        for  i in range(1,self.value):
            if self.value%i==0:
                sum1=sum1+i
        print("Sum of factors are:",sum1)
        if sum1==self.value:
            return True
        else:
            return False
    
    def Factors(self):
        factors=[]
        for  i in range(1,self.value):
            if self.value%i==0:
                factors.append(i)
        print("Factors of no is :",factors)
    
    def SumFactor(self):
        sum1=0
        for  i in range(1,self.value):
            if self.value%i==0:
                sum1=sum1+i
        print("Sum of factors are:",sum1)

n1=Number()
print("Prime no:",n1.ChkPrime())
print("Perfect no:",n1.ChkPerfect())
n1.Factors()
n1.SumFactor()