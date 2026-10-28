
# Lesson 04 — Network Automation with Netmiko

## Objective
Automate SSH connections to Cisco network devices using Python and Netmiko.

## Lab Environment
- R1: Cisco CSR1000V
- S2: Cisco IOSv L2
- Python 3.13
- Netmiko
- PNETLab

## What I Learned
- Defining network devices using a list of dictionaries
- Establishing SSH connections with Netmiko
- Executing multiple show commands automatically
- Using loops to process devices and commands
- Handling connection and command errors with try/except
- Closing SSH sessions with finally
- Generating timestamped reports using datetime and file handling

## Commands Collected
- show version
- show running-config | include hostname
- show ip interface brief
- show inventory

## How to Run
1. Install Python and Netmiko.
2. Update the device IP addresses and credentials.
3. Run:

   python netmiko_first_connection.py

## Security
Never publish real passwords, sensitive network information, or device reports.

