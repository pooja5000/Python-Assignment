# Write a lambda function which accepts one number and returns True if number is even otherwise False.

no=int(input("Enter number:"))

chkeven=lambda no:no%2==0

# ret=chkeven(no)
# print(ret)

print(chkeven(no))