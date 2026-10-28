from netmiko import ConnectHandler
from datetime import datetime

# Create a timestamp for the report filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

report_file = f"network_report_{timestamp}.txt"

devices = [
   { 
    "device_type": "cisco_ios",
    "host": "192.168.56.145",
    "username": "pnetlab",
    "password": "YOUR_SWITCH_PASSWORD"
   
    },
    {
    "device_type": "cisco_ios",
    "host": "192.168.56.144",
    "username": "pnetlab",
    "password": "YOUR_ROUTER_PASSWORD"
   
    },
]
# Commands we want to execute
commands = [
    "show version",
    "show running-config | include hostname",
    "show ip interface brief",
    "show inventory",
]

# Open the report file for writing
with open(report_file, "w", encoding="utf-8") as report:

    report.write("NETWORK DEVICE COLLECTION REPORT\n")
    report.write(f"Generated: {datetime.now()}\n")
    report.write("=" * 70 + "\n")

    # Connect to each device
    for device in devices:
        print(f"\nConnecting to {device['host']}")

        report.write(f"\nDevice IP: {device['host']}\n")
        report.write("=" * 70 + "\n")

        connection = None

        try:
            connection = ConnectHandler(**device)

            hostname = connection.find_prompt().strip("#>")
            print(f"Connected to {hostname}")

            report.write(f"Hostname: {hostname}\n")

            # Execute each command
            for command in commands:
                print(f"Collecting: {command}")

                report.write(f"\n--- {command} ---\n")

                try:
                    output = connection.send_command(command)
                    report.write(output + "\n")

                except Exception as error:
                    error_message = f"Command failed: {error}"
                    print(error_message)
                    report.write(error_message + "\n")

        except Exception as error:
            error_message = (
                f"Connection failed to {device['host']}: {error}"
            )
            print(error_message)
            report.write(error_message + "\n")

        finally:
            if connection:
                connection.disconnect()

    report.write("\nDevice collection completed.\n")

print(f"\nDevice collection completed.")
print(f"Report saved to: {report_file}")



