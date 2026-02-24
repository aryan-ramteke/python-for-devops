import psutil

#function : to check cpu health based on the threshold
def cpu_health(cpu_thresh) :
    print("CPU Threshold is :",cpu_thresh)
    cpu_per = psutil.cpu_percent(interval=1)
    print("CPU utilisation is : ",cpu_per)
    if cpu_thresh < cpu_per :
        print("CPU utilisation is more than the threshold")
    else :
        print("CPU utilisation is less than the threshold")
       
#checking storage usage
def disk_health(disk_thresh) :
    print("Disk Threshold is :",disk_thresh)
    disk_usage_per = psutil.disk_usage("C:")[3]
    print("Disk utilisation is : ",disk_usage_per)
    if disk_thresh < disk_usage_per :
        print("Disk utilisation is more than the threshold")
    else :
        print("Disk utilisation is less than the threshold") 
        
#checking RAM usage
def mem_health(mem_thresh) :
    print("Memory Threshold is :",mem_thresh)
    mem_usage_per = psutil.virtual_memory()[2]
    print("RAM utilisation is : ",mem_usage_per)
    if mem_thresh < mem_usage_per :
        print("RAM utilisation is more than the threshold")
    else :
        print("RAM utilisation is less than the threshold") 
        
#take sys metric's thresholds from user
try :
    cpu_thresh = float(input("Enter CPU threshold: "))
    disk_thresh = float(input("Enter disk threshold: "))
    mem_thresh = float(input("Enter memory utilisation: "))
    cpu_health(cpu_thresh)

    #take disk threshold from user

    disk_health(disk_thresh)

    #take memory threshold

    mem_health(mem_thresh)
except (ValueError) as v:
    print(v)
except Exception as e :
    print(e)
    

