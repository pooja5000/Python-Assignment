# Write a lambda function which accepts two numbers and returns addition.
no1=int(input("Enter first number:"))
no2=int(input("Enter second number:"))

add=lambda no1,no2:no1+no2
result=add(no1,no2)
print("Addition is:",result)