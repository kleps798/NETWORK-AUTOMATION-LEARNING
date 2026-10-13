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

for device in devices:
    if device["status"] == "DOWN":
        down_count = down_count + 1
        print(f"{device["hostname"]} | {device["status"]} | DEVICE DOWN")

    elif device["cpu_usage"] < 70:
        print(f"{device['hostname']} | {device['status']} | CPU NORMAL")
    else:
        print(f"{device['hostname']} | {device['status']} | HIGH CPU")

print (f"DEVICES DOWN: {down_count}")

    


        
             







