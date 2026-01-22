# Write a lambda function which accepts two numbers and returns maximum number.
no1=int(input("Enter firt no:"))
no2=int(input("Enter second no:"))
max=lambda no1,no2:no1>no2

ret=max(no1,no2)

if ret==True:
    print("Max no is:",no1)

else:
    print("Max no is:",no2)