# 3. Design automation script which accept directory name and delete all duplicate files from that
#  directory. Write names of duplicate files from that directory into log file named as Log.txt. 
# Log.txt file should be created into current directory.
# Usage: Directory Dusplicate Removal.py "Demo"
# Demo is name of directory

import os
import hashlib
import sys

def getchecksum(file):
    hobj=hashlib.md5()
    fobj=open(file,"rb")

    while True:
        data=fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    return hobj.hexdigest()

    
    
def dublicate(Directory_name):
    dict1={}
    if os.path.exists(Directory_name)==False:
        print("No such directory")
        return
    if os.path.isdir(Directory_name)==False:
        print("This is not directory")
        return
    
    
    for folder,subfolder,files in os.walk(Directory_name):
        for file in files:
            filename=os.path.join(Directory_name,file)
            ret=getchecksum(filename)

            if ret in dict1:
                dict1[ret].append(filename)

            else:
                dict1[ret]=[filename]
        #print(dict1)
    dublicate=[]
    for value in dict1.values():
        if len(value)>1:
            dublicate.append(value)
    
    print(dublicate)
    
    
    
    fobj=open("marvellous.log",'w')
    fobj.write("------------------Assignment32_2 Start--------------------\n")
    fobj.write("Dublicate file are:\n ")
    for filename in dublicate:
        for file in filename:
            fobj.write(file+"\n")

    count=0
    fobj.write("Removed duplicate files:\n")
    for filename in dublicate:  
       for file in filename:
           count=count+1
           if(count>1):
                fobj.write(file+"\n")
                os.remove(file)
       count=0
        


        
    fobj.write("------------------Assignment32_2 End--------------------\n")
        





















        



        



            

        

    
    
    

        


def main():
    
    if len(sys.argv)==2:
        dublicate(sys.argv[1])
        
    else:
        print("Invalid arguments")

if __name__=="__main__":
    main()