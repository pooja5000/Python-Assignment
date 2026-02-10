# 3. Design automation script which accept two directory names. Copy all files from first directory into second directory. 
# Second directory should be created at run time.
# Usage: Directory Copy.py "Demo" "Temp"
# Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files from Demo to Temp.
import os
import sys
import shutil

def CopyFiles(Directory1,Directory2):

    ret=os.path.exists(Directory1)
    if ret==False:
        print("Directory is not available")
        return
    
    ret=os.path.isdir(Directory1)
    if ret==False:
        print("This is not Directory")
        return
    
    ret=os.path.exists(Directory2)
    if ret==False:
       os.makedirs(Directory1,exist_ok=True)

    fobj=open("Marvellous1.log",'w')

    fobj.write("---------Assignment 31----------\n")

    print("Directory created successfully")
    for folder ,subfolder, file in os.walk(Directory1):
        for fname in file:
            src=os.path.join(folder,fname)
            relative=os.path.relpath(src,Directory1)
            dest=os.path.join(Directory2,relative)
            
            os.makedirs(os.path.dirname(dest),exist_ok=True)
            shutil.copy2(src,dest)

            fobj.write("%s Copied into:%s\n"%(src,dest))

def main():

    if len(sys.argv)==3:
        CopyFiles(sys.argv[1],sys.argv[2])
    else:
        print("Invalid no of arguments")

if __name__=="__main__":
    main()
    

    


