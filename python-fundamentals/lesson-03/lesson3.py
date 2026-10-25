# Python Fundamentals - Lesson 3
# Dictionaries
# Network Automation Learning Journey

device = {
    "hostname": "CORE-RTR-01",
    "ip_address": "10.10.10.1",
    "vendor": "cisco",
    "device_type": "router",
    "ios_version": "17.9.4",
    "status": "UP",
    "cpu_usage": 37.5

}

device2 ={
    "hostname": "CORE-SW-01",
    "ip_address": "10.10.10.10",
    "vendor": "cisco",
    "device_type": "switch",
    "ios_version": "17.12.4",
    "status": "DOWN",
    "cpu_usage": 80.5
    }

devices = [device, device2]

down_count = 0
high_cpu_count = 0
critical_cpu_count = 0

for device in devices:
    if device["status"] == "DOWN":
        down_count = down_count + 1
        print(f"{device['hostname']} | {device['status']} | DEVICE DOWN")    

    elif device["cpu_usage"] < 70:
        print(f"{device['hostname']} | {device['status']} | CPU NORMAL")
    else:
        print(f"{device['hostname']} | {device['status']} | HIGH CPU")

# Independent CPU counter          

    if device["cpu_usage"] >= 90:
        critical_cpu_count = critical_cpu_count + 1 
       

    elif device["cpu_usage"] >= 70:
        high_cpu_count = high_cpu_count + 1
        
    else:
        print(f"CPU NORMAL: {device['cpu_usage']}")

           

print (f"DEVICES DOWN: {down_count}")
print(f"CRITICAL CPU DEVICES: {critical_cpu_count}")
print(f"HIGH CPU DEVICES: {high_cpu_count}")



    


        
             







