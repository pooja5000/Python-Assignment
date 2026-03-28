import os
import shutil
import hashlib
import zipfile

def CalChecksum(file):

    hobj=hashlib.md5()

    fobj=open(file,"rb")

    while True:
        data=fobj.read(1024)
        hobj.update(data)
        if not data:
            break

    return hobj.hexdigest()



def Logging_System(DirectoryName,backup_folder):
    
    os.makedirs(DirectoryName,exist_ok=True)
    os.makedirs(backup_folder,exist_ok=True)
    copiedfile=[]
    

    for folder,subfolder,file in os.walk(DirectoryName):
        for f in file:
            

            sorcepath=os.path.join(DirectoryName,f)
            relattive=os.path.relpath(sorcepath,DirectoryName)
            destinationpath=os.path.join(backup_folder,relattive)

            if not os.path.exists(destinationpath):
                shutil.copy2(sorcepath,destinationpath)

            elif CalChecksum(sorcepath)!=CalChecksum(destinationpath):
                shutil.copy2(sorcepath,destinationpath)
    
            copiedfile.append(relattive)
    return copiedfile

def zipmaker(backup):

    archive="BKP.zip"
    zip1=zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED)

    for folder,subfolder,file in os.walk(backup):
        for f in file:
            fullpath=os.path.join(backup,f)
            relative=os.path.relpath(fullpath,backup)

            zip1.write(fullpath,relative)

    zip1.close()
            
            



    

        

def main():
    Logging_System("log","Backup")
    zipmaker("Backup")
if __name__=="__main__":
    main()
     

    