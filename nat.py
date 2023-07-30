from netmiko import ConnectHandler
from datetime import datetime
from time import sleep
from colorama import Back, Fore, Style
import re

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.0.172",
    "username": "admin",
    "password": "password",
}

def nat_check():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    net_connect = ConnectHandler(**device)
    command = "show ip nat translations | i 128.128.0.2"
    output = net_connect.send_command(command)

    if output:
        nats = output.split()
        nat1 = nats[1]
        nat2 = nats[2]
        nat3 = nats[3]
        nat4 = nats[4]
        nat0 = nats[0]
        #print([nats[i] for i in (1,2,3,4,0)])
        linia = (f"[{current_time}]--[{nat0}]--[{nat2}]--[{nat1}]--[{nat3}]--[{nat4}]")
        print(f'[{Fore.YELLOW}{current_time}{Fore.WHITE}]  [{Fore.GREEN}{nat0}{Fore.WHITE}]  [{Fore.RED}{nat2}{Fore.WHITE}]-->[{nat1}]-->[{Fore.RED}{nat4}{Fore.WHITE}]  [{Fore.GREEN}USER{Fore.WHITE}]')
        file = open("nat.txt", 'a')
        if "128.128.0.2" in linia:
                file.write(linia + "\n")
                file.close()
        net_connect.disconnect()
    else:
        net_connect.disconnect()
        pass


nat_check()

while True:
    nat_check()
    sleep(10)




#todosy:
#user z ise na podstawie source ip
#dest ip z palo
#user ck w AD
