# 1. Design automation script which accept directory name and display checksum of all files.
# Usage: DirectoryChecksum.py "Demo"
# Demo is name of directory.

import os
import hashlib
import sys

def checksum(Directory_name):

    ret=os.path.exists(Directory_name)
    if ret==False:
        print("This directory is not present")
        return
    
    ret=os.path.isdir(Directory_name)
    if ret==False:
        print("This is not directory")
        return
    
    hobj=hashlib.md5() 
    fobj1=open("marvellous.log",'w')
    fobj1.write("--------------Assignement 32 Start-------------------\n")
    for folder,subfolder,file in os.walk(Directory_name):

        for fname in file:
            filename=os.path.join(Directory_name,fname)
            fobj=open(filename,"rb")

            while True:
                data=fobj.read(1024)
                if not data:
                    break
                else:
                    hobj.update(data)

            calculatechecksum=hobj.hexdigest()
            fobj1.write(fname+":"+calculatechecksum+"\n")

   
    
    fobj1.write("--------------Assignement 32 End---------------------")

def main():
    
    if len(sys.argv)==2:
        checksum(sys.argv[1])
        
    else:
        print("Invalid arguments")

if __name__=="__main__":
    main()