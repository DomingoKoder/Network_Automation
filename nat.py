import paramiko
import re
from datetime import datetime
from time import sleep
from tabulate import tabulate

router_ip = "192.168.0.172"
router_username = "admin"
router_password = "password"

protocols = ['tcp', 'udp', 'icmp', 'esp', 'pptp', 'rsvp']



def nat_check():
    
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()

    now = datetime.now()
    current_time = now.strftime("[ %H:%M:%S ]   ")

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(router_ip, 
                username=router_username, 
                password=router_password,
                look_for_keys=False)

    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show ip nat translations | i 10.0.0")
    output = ssh_stdout.readlines()
    #wywalenie blank line przed
    for linijka in output:
        linijka=linijka.rstrip()

    linia = current_time.join(output)
    linia = linia.strip()
    
    file = open("nat.txt", 'a')
    if "10.0.0" in linia:
        file.write(linia + "\n")
        file.close()
    ssh.close()
    print(linia)

nat_check()

while True:
    nat_check()
    sleep(10)


#time.sleep(1.30)









