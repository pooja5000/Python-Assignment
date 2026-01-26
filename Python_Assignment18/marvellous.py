from math import sqrt
def ChkPrime(item):
    if item<=1:
        return False
    
    for i in range(2,int(sqrt(item))+1):
        if item%i==0:
            return False

    return True