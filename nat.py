import paramiko
from datetime import datetime
from time import sleep


USER = "bw76qilsa"
PASSWORD = "wKGF/Y{<qgKM!4$s"
router_ip = "10.112.204.22"


def nat_check():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()

    now = datetime.now()
    current_time = now.strftime("[ %H:%M:%S ]   ")

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(router_ip, 
                username=USER, 
                password=PASSWORD,
                look_for_keys=False)


    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show ip nat translations | i 63.117.68.")
    output = ssh_stdout.readlines()
    output = "\n".join(entry for entry in str(output).splitlines() if entry.strip())
    if not output:
        linia = f"{current_time} Output not found"
    else:
        linia = current_time.join(output)
    
    file = open("nat.txt", 'a')

    if "63.117.68." in linia:
        file.write(linia)
        file.close()

    ssh.close()

while True:
    nat_check()
    sleep(3600)

#from keyring import get_password
#PASSWORD = get_password("LSA", LSA)
#logger





