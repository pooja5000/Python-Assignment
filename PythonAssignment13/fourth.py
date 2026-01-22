#Write a program which accepts one number and prints binary equivalent.
def binary(no):
    bin=[]
    while no>0:
        
        bin.append(no%2)
        no=no//2
        
        

    return bin



def main():
    ret=binary(15)
    print(ret)
    print(len(ret))
    data=[]
    for i in range(len(ret)-1,-1,-1):
        data.append(ret[i])
    print("Binary equivalent is:",data)
        
        

if __name__=="__main__":
    main()