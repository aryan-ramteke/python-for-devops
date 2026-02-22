import psutil

#function : to check cpu health based on the threshold
def cpu_health(cpu_thresh) :
    print("CPU Threshold is :",cpu_thresh)
    cpu_per = psutil.cpu_percent(interval=1)
    print("CPU utilisation is : ",cpu_per)
    if int(cpu_thresh) < cpu_per :
        print("CPU utilisation is more than the threshold")
    else :
        print("CPU utilisation is less than the threshold")
       
#checking storage usage
def disk_health(disk_thresh) :
    print("Disk Threshold is :",disk_thresh)
    disk_usage_per = psutil.disk_usage("C:")[3]
    print("Disk utilisation is : ",disk_usage_per)
    if int(disk_thresh) < disk_usage_per :
        print("Disk utilisation is more than the threshold")
    else :
        print("Disk utilisation is less than the threshold") 
        
#checking RAM usage
def mem_health(mem_thresh) :
    print("Memory Threshold is :",mem_thresh)
    mem_usage_per = psutil.virtual_memory()[2]
    print("RAM utilisation is : ",mem_usage_per)
    if int(mem_thresh) < mem_usage_per :
        print("RAM utilisation is more than the threshold")
    else :
        print("RAM utilisation is less than the threshold") 
        
#take cpu threshold from user
cpu_thresh = input("Enter CPU threshold: ")
cpu_health(cpu_thresh)

#take disk threshold from user
disk_thresh = input("Enter disk threshold: ")
disk_health(disk_thresh)

#take memory threshold
mem_thresh = input("Enter memory utilisation: ")
mem_health(mem_thresh)