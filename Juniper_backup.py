from netmiko import ConnectHandler
from datetime import datetime
import os

def take_backup(device, backup_directory):
    connection = None  # Initialize the connection variable
    try:
        # Establish connection to the device
        print(f"Connecting to {device['host']}...")
        connection = ConnectHandler(**device)
        print(f"Connected to {device['host']}.")

        # Fetch the hostname
        hostname_output = connection.send_command('show configuration system host-name | display set | no-more')
        hostname = hostname_output.split()[-1]  # Extract hostname from the output

        # Send command to get configuration
        print(f"Fetching configuration from {hostname}...")
        config = connection.send_command('show configuration | display set | no-more')

        # Create a unique backup file name based on the hostname and current date/time
        current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = os.path.join(backup_directory, f"{hostname}_{current_datetime}.txt")

        # Save the configuration to a file
        with open(backup_file, 'w') as file:
            file.write(config)

        print(f"Backup for {hostname} saved to {backup_file}")

    except Exception as e:
        print(f"An error occurred with {device['host']}: {e}")

    finally:
        # Close the connection if it was successfully established
        if connection:
            print(f"Disconnecting from {device['host']}...")
            connection.disconnect()
            print(f"Disconnected from {device['host']}.")

# List of device IP addresses
device_ips = ['172.28.100.4' '172.28.100.5' '172.28.100.6']

# Replace with your credentials and backup directory path
backup_directory = '/root/network/backups/Test'
username = 'admin'
password = 'admin123'

# Ensure the backup directory exists
if not os.path.exists(backup_directory):
    os.makedirs(backup_directory)

# Loop through each device and take a backup
for ip in device_ips:
    device = {
        'device_type': 'juniper',
        'host': ip,
        'username': username,
        'password': password,
        'port': 22,  # Specify the SSH port here
    }
    take_backup(device, backup_directory)
