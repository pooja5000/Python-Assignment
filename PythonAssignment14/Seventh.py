# Write a lambda function which accepts one number and returns True if divisible by 5.

no=int(input("Enter number:"))

divbyfive=lambda no:no%5==0

# ret=chkeven(no)
# print(ret)

print(divbyfive(no))