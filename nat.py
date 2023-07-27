import paramiko
from datetime import datetime

router_ip = "192.168.0.172"
router_username = "admin"
router_password = "password"

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
linia = current_time.join(output)
file = open("nat.txt", 'a')

if "10.0.0" in linia:
    file.write(linia)
    file.close()

#time.sleep(1.30)

ssh.close()







