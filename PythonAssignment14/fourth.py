# Write a lambda function which accepts two numbers and returns minimum number.
no1=int(input("Enter no1:"))
no2=int(input("Enter no2"))
min=lambda no1,no2:no1<no2
ret =min(no1,no2)
if ret==True:
    print("Minimun no is:",no1)
else:
    print("Minimun no is:",no1)