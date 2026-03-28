# 1. Add Thread Monitoring Feature
# For each running process, display:
# Process Name
# PID
# Number of Threads created by that process
# Requirement
# Store information in log file along with timestamp.
# --------------------------------------------------------------------------------------------------
# 2. Add Open Files Monitoring Feature
# For each process, display:
# Number of files opened by the process
# Requirement
# Count open file descriptors using system/library calls
# Handle permission errors properly
# Mention "Access Denied" in log if required
#-----------------------------------------------------------------------------------------------------
# 3. Add Actual Memory Allocation Feature
# Display real memory usage of each process:
# RSS (Resident Set Size-actual RAM used)
# VMS (Virtual Memory)
# Memory Percentage
# Requirement
# Show:
# .
# Top 10 memory consuming processes

import psutil
import time
import schedule
import smtplib
import sys
from email.message import EmailMessage

def MailSender(receiver,file):
    msg=EmailMessage()
    body=ProcessSummery()
    
    msg["From"]="poojapgaikwad1@gmail.com"
    msg["To"]=receiver
    msg["Subject"]="Marvellous Platform servillence report"
    
    msg.set_content(body)
    f=open(file,"rb")
    data=f.read()
    f.close()
    
    msg.add_attachment(data,maintype="application",subtype="octet-stream",filename=file)
    
    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

    # 5. login using gmail + app password 
    smtp.login("poojapgaikwad1@gmail.com","sccz rcen nhvr qfvg")

    # 6. send the email
    smtp.send_message(msg)

     # 7. Close connection manually
    smtp.quit()



def Log_file(file,receiver):
    border="-"*40
    timestamp=time.strftime("_%Y-%m-%d_%H-%M-%S")
    filename=file+timestamp
    fobj=open(filename,'w')
    procinfo=ActualMemoryAllocationFeature()

    for data in procinfo:
        fobj.write("\n Process id is:"+str(data.get('pid'))+"\n")
        fobj.write("Process Name is :"+data.get('name')+"\n")
        fobj.write("No of threads created by process:"+str(data.get('num_thraeds'))+"\n")
        fobj.write("Ram usage:"+str(data.get('RSS'))+"\n")
        fobj.write("Virtual memory usage is:"+str(data.get('vms'))+"\n")
        fobj.write("Memory usage:"+str(data.get('Memory'))+"\n")
        fobj.write("No of open files are:"+str(data.get('count'))+"\n")
        fobj.write(border)
    
    procinfo.sort(key=lambda x:x['RSS'],reverse=True)
    fobj.write("-------------------------Top 10 High memory consuming ------------------------")
    for data in procinfo[:10]:
        fobj.write("\n Process id is:"+str(data.get('pid'))+"\n")
        fobj.write("Process Name is :"+data.get('name')+"\n")
        fobj.write("No of threads created by process:"+str(data.get('num_thraeds'))+"\n")
        fobj.write("Ram usage:"+str(data.get('RSS'))+"\n")
        fobj.write("Virtual memory usage is:"+str(data.get('vms'))+"\n")
        fobj.write("Memory usage:"+str(data.get('Memory'))+"\n")
        fobj.write("No of open files are:"+str(data.get('count'))+"\n")
        fobj.write(border)
    fobj.close()

    MailSender(receiver,filename)        
  
def ActualMemoryAllocationFeature():
    counter=0
    proessinfo=[]
    for proc in psutil.process_iter(attrs=['pid','name','num_threads']):

        try:

            information=proc.info
            mem=proc.memory_info()
            RAMInMB=round(mem.rss/(1024.0*1024.0),2)
            
            virtulmem=round(proc.memory_info().vms/(1024.0*1024.0),2)
            information['RSS']=RAMInMB
            information['vms']=virtulmem
            information['Memory']=proc.memory_percent()
            open_files=proc.open_files()
            counter=counter+1
            information['count']=counter

            proessinfo.append(information)
        except(FileNotFoundError,psutil.AccessDenied,Exception):
            continue

            

        except(psutil.NoSuchProcess):
            pass

    proessinfo.sort(key=lambda x:x['RSS'],reverse=True)
    return proessinfo

def ProcessSummery():
    procsummery=ActualMemoryAllocationFeature()
    summery=[]


    rss=sorted(procsummery,key=lambda x:x["RSS"],reverse=True)
    memory=sorted(procsummery, key=lambda x:x["Memory"],reverse=True)
    numthreads=sorted(procsummery,key=lambda x:x["num_threads"],reverse=True)
    openfile=sorted(procsummery,key=lambda x:x['count'],reverse=True)

    summery.append("Total processes:"+str(len(procsummery)))
    summery.append("Top CPU usage processes:"+memory[0]['name'])
    summery.append("Top Memory usage processes:"+rss[0]['name'])
    summery.append("Top Thread count processes:"+numthreads[0]['name'])
    summery.append("Top open file proe=cess:"+openfile[0]['name'])

    return "\n".join(summery)

def main():
   
    if len(sys.argv)==4:

        schedule.every(int(sys.argv[3])).minutes.do(Log_file,sys.argv[1],sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid no of arguments")
    

if __name__=="__main__":
    main()




