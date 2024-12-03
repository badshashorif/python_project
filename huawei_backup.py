from netmiko import ConnectHandler
import time
import re
import os

# List of IP addresses for the Huawei devices
devices = ["192.168.100.52", "192.168.100.57", "192.168.100.58", "192.168.100.109", "192.168.100.130", "192.168.100.108", "192.168.100.2"]

# Telnet login credentials
username = "admin"
password = "admin"

# Backup destination directory
backup_directory = "/root/network/backups/HUAWEI"

# Ensure the backup directory exists
if not os.path.exists(backup_directory):
    os.makedirs(backup_directory)

# Function to perform backup from each device
def backup_huawei_switch(ip):
    net_connect = None  # Initialize connection variable
    try:
        # Huawei device definition for Telnet
        huawei_switch = {
            'device_type': 'huawei_telnet',
            'host': ip,
            'username': username,
            'password': password,
            'port': 23,  # Telnet port
            'timeout': 60,  # Increase timeout
            'banner_timeout': 60,  # Allow more time for device banners
            'global_delay_factor': 2,  # Global delay for command execution
        }

        # Connect to the device via Telnet
        print(f"Connecting to {ip} via Telnet...")
        net_connect = ConnectHandler(**huawei_switch)

        # Fetch interface description
        print(f"Fetching interface description from {ip}...")
        interface_output = net_connect.send_command('display interface description', expect_string=r'>')

        # Fetch current configuration and handle pagination
        print(f"Fetching current configuration from {ip}...")
        config_output = net_connect.send_command_timing('display current-configuration', delay_factor=2)

        # Continue fetching configuration until no "More" prompt appears
        while '---- More ----' in config_output:
            config_output += net_connect.send_command_timing(' ', delay_factor=2)

        # Search for the sysname in the configuration
        sysname_search = re.search(r'sysname\s+(\S+)', config_output)  # Look for sysname <hostname>
        if sysname_search:
            sysname = sysname_search.group(1)  # Extract sysname value
        else:
            sysname = f"unknown_{ip}"  # Fallback if sysname is not found

        # Use sysname to create unique backup filenames with timestamp
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        backup_filename = f"{backup_directory}/{sysname}_{timestamp}.txt"

        # Write both outputs to the same file with clear sections
        with open(backup_filename, "w") as backup_file:
            backup_file.write(f"==== Interface Description ====\n{interface_output}\n")
            backup_file.write(f"\n==== Current Configuration ====\n{config_output}\n")

        print(f"Backup successful for {sysname} ({ip}). Data saved to {backup_filename}")

    except Exception as e:
        print(f"Error connecting to {ip}: {e}")

    finally:
        if net_connect:
            # Only attempt to disconnect if the connection was successful
            net_connect.disconnect()

# Iterate through all devices and back up the configurations
for ip in devices:
    backup_huawei_switch(ip)
