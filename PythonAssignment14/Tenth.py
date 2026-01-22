# Write a lambda function which accepts two numbers and returns maximum number.
no1=int(input("Enter firt no:"))
no2=int(input("Enter second no:"))
no3=int(input("Enter third no:"))


largest=lambda no1,no2,no3:no1 if no1>no2 and no1>no3 else (no2 if no2>no1 and no2>no3 else no3)

print(largest(no1,no2,no3))