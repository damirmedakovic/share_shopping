from pexpect import pxssh
import getpass
import time

#dmedakovic@74.207.252.20
try:
    s = pxssh.pxssh()

    hostname = ''
    username = ''
    password = ''
    
    s.login(hostname, username, password)
   

    
    name = "share_shopping"
    ACTOKEN = ''

    s.sendline('find -delete')
    s.prompt()
    print(s.before)

    s.sendline(f'git clone https://oauth2:{ACTOKEN}@gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-3.git {name}')
    s.prompt()
    print(s.before)

    s.sendline(f'cd {name}/handleliste')
    s.prompt()
    print(s.before)
    
    s.sendline('python3 -m pip install django')
    s.prompt()
    print(s.before)


    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)

   

