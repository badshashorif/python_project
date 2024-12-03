

import paramiko
import time

print("")
print("  People Internet (ISP) - Queue Script   ")
print("")
print("     0 : Unlimited ")
print("     1 : Peak ")
print("     2 : Off-Peak ")
print("     3 : Off-Peak-50-Percent ")
print("     4 : BONUS  ")
print("     5 : DOUBLE_OFF-PEAK ")
print("")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

hq_nat = {'hostname': '10.60.80.2', 'port': '22', 'username':'admin', 'password':'admin'}
uttaranat = {'hostname': '10.60.80.6', 'port': '22', 'username':'admin', 'password':'admin'}
greenroadnat = {'hostname': '10.60.80.10', 'port': '22', 'username':'admin', 'password':'admin'}
jamuna = {'hostname': '10.60.80.14', 'port': '22', 'username':'admin', 'password':'admin'}
nat_rtr_hq_02 = {'hostname': '10.60.80.22', 'port': '22', 'username':'admin', 'password':'admin'}


mirpurboro = {'hostname': '192.168.100.9', 'port': '22', 'username':'admin', 'password':'admin'}
dhakauddan = {'hostname': '192.168.100.14', 'port': '22', 'username':'admin', 'password':'admin'}
banani = {'hostname': '192.168.100.15', 'port': '22', 'username':'admin', 'password':'admin'}
hq = {'hostname': '192.168.100.17', 'port': '22', 'username':'admin', 'password':'admin'}
dhanmondi = {'hostname': '192.168.100.21', 'port': '22', 'username':'admin', 'password':'admin'}
modhubazar = {'hostname': '192.168.100.22', 'port': '22', 'username':'admin', 'password':'admin'}
monshurabad = {'hostname': '192.168.100.24', 'port': '22', 'username':'admin', 'password':'admin'}
bosila = {'hostname': '192.168.100.25', 'port': '22', 'username':'admin', 'password':'admin'}
jigatola = {'hostname': '192.168.100.26', 'port': '22', 'username':'admin', 'password':'admin'}
basundhara = {'hostname': '192.168.100.27', 'port': '22', 'username':'admin', 'password':'admin'}
tejkunipara = {'hostname': '192.168.100.28', 'port': '22', 'username':'admin', 'password':'admin'}
nimtola = {'hostname': '192.168.100.29', 'port': '22', 'username':'admin', 'password':'admin'}
jamunafuturepark = {'hostname': '192.168.100.35', 'port': '22', 'username':'admin', 'password':'admin'}
tajhmohol = {'hostname': '192.168.100.31', 'port': '22', 'username':'admin', 'password':'admin'}
atibazar = {'hostname': '192.168.100.34', 'port': '22', 'username':'admin', 'password':'admin'}
shamoly = {'hostname': '192.168.100.11', 'port': '22', 'username':'admin', 'password':'admin'}
mohammadpur = {'hostname': '192.168.100.16', 'port': '22', 'username':'admin', 'password':'admin'}
niknet = {'hostname': '192.168.100.12', 'port': '22', 'username':'admin', 'password':'admin'}
sadek_rode = {'hostname': '192.168.100.37', 'port': '22', 'username':'admin', 'password':'admin'}
uttara_12 = {'hostname': '192.168.100.36', 'port': '22', 'username':'admin', 'password':'admin'}
dhanmondi_14_a = {'hostname': '192.168.100.38', 'port': '22', 'username':'admin', 'password':'admin'}
badda = {'hostname': '192.168.100.39', 'port': '22', 'username':'admin', 'password':'admin'}



routers = [ nat_rtr_hq_02, hq_nat, uttaranat, greenroadnat, mirpurboro, dhakauddan, banani, hq, dhanmondi, mohammadpur, modhubazar, monshurabad, bosila, jigatola, basundhara, tejkunipara, nimtola, jamunafuturepark, tajhmohol, atibazar, shamoly, niknet, jamuna, sadek_rode, uttara_12, dhanmondi_14_a, badda]

script_id = input("Enter Script Value : ")
    
for router in routers:

    print(f'Connected to {router["hostname"]}')
    print("")
    client.connect(**router)

    stdin, stdout, stderr = client.exec_command(f'system script run {script_id}')
    for line in stdout:
        print(line.strip('\n'))
        
client.close()



