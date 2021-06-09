import base64
import os
import time
import subprocess
from getpass import getpass
import random
from hashlib import *
import base64
try:
    import pyfiglet
    import ascii_magic
    
except:
    os.system("pip install pyfiglet")
    os.system("pip install ascii_magic")
os.system("cls")
time.sleep(2)
qwer=("kali.png")
out=ascii_magic.from_image_file(qwer,columns=150,char=']')
ascii_magic.to_terminal(out)
time.sleep(2)
os.system("cls")
print("""
 _
| |   (_)_ __  _   ___  __
| |   | | '_ \| | | \ \/ /
| |___| | | | | |_| |>  <
|_____|_|_| |_|\__,_/_/\_\   v2""")
print("")
print("""
                     \033[0;38 ───────────────────────────
                    \033[0;38m|                           |
                    \033[0;38m|\033[0;31m         </AL7>            \033[0;38m|
                    \033[0;38m| \033[0;34mTwitter:@alhassanAlharb7  \033[0;38m|
                    \033[0;38m|\033[0;31m        Terminal           \033[0;38m|
                    \033[0;38m|___________________________|""")
username=input("User name: ")
password=getpass("Password: ")
print("""
kali_linux Theme [1]
ubuntu Theme [2]
AL7 Theme [3]""")
theme=input("Theme >> ")



#def___
def neofetch_AL7():
    if command=="neofetch":
        print("\033[0;35m")
        pyfiglet.print_figlet("</AL7>")

def neofetch_kali():
    if command=="neofetch":
     print(f"""\033[0;34m
\033[0;34m..............                                     {username}\033[0;37m@\033[0;34mkali\033[0;37m
\033[0;34m            ..,;:ccc,.                             \033[0;37m______________             
\033[0;34m          ......''';lxO.                           \033[0;37mOS: Kali GNU/Linux
\033[0;34m.....''''..........,:ld;                           \033[0;37mShell: bash & Python
\033[0;34m           .';;;:::;,,.x,                          \033[0;37mTerminal: Terminal
\033[0;34m      ..'''.            0Xxoc:,.  ...           
\033[0;34m  ....                ,ONkc;,;cokOdc',.      
\033[0;34m .                   OMo           ':ddo.                     
\033[0;34m                    dMc               :OO;     
\033[0;34m                    0M.                 .:o          
\033[0;34m                    ;Wd               
\033[0;34m                     ;XO,     
\033[0;34m                       ,d0Odlc;,.. 
\033[0;34m                           ..',;:cdOOd::,. 
\033[0;34m                                    .:d;.':;.             
\033[0;34m                                       'd,  .'   
\033[0;34m                                         ;l   ..  
\033[0;34m                                          .o     
\033[0;34m                                            c                                
\033[0;34m                                            .'                               
\033[0;34m                                             .                               """)
def neofetch_ubuntu():
    if command=="neofetch":
        a=[f"""\033[0;34m
            .-/+oossssoo+/-.               {username}@linux
        `:+ssssssssssssssssss+:`           ----------------------
      -+ssssssssssssssssssyyssss+-         OS: \033[0;37mUbuntu Terminal\033[0;34m
    .ossssssssssssssssss\033[0;37mdMMMNy\033[0;34msssso.       Kernel: \033[0;37m</AL7>\033[0;34m
   /sssssssssss\033[0;37mhdmmNNmmyNMMMMh\033[0;34mssssss/
  +sssssssss\033[0;37mhm\033[0;34myd\033[0;37mMMMMMMMNddddy\033[0;34mssssssss+     Shell: \033[0;37mbash & Python 3\033[0;34m
 /ssssssss\033[0;37mhNMMM\033[0;34myh\033[0;37mhyyyyhmNMMMNh\033[0;34mssssssss/    Terminal: \033[0;37mGnom\033[0;34m
.ssssssss\033[0;37mdMMMNh\033[0;34mssssssssss\033[0;37mhNMMMd\033[0;34mssssssss.   
+ssss\033[0;37mhhhyNMMNy\033[0;34mssssssssssss\033[0;37myNMMMy\033[0;34msssssss+   
oss\033[0;37myNMMMNyMMh\033[0;34mssssssssssssss\033[0;37mhmmmh\033[0;34mssssssso 
oss\033[0;37myNMMMNyMMh\033[0;34mssssssssssssssmhmmmh\033[0;34mssssssso
+ssss\033[0;37mhhhyNMMNy\033[0;34mssssssssssss\033[0;37myNMMMy\033[0;34msssssss+
.ssssssss\033[0;37mdMMMNh\033[0;34mssssssssss\033[0;37mhNMMMd\033[0;34mssssssss.
 /ssssssss\033[0;37mhNMMM\033[0;34myh\033[0;37mhyyyyhdNMMMNh\033[0;34mssssssss/
  +sssssssss\033[0;37mdm\033[0;34myd\033[0;37mMMMMMMMMddddy\033[0;34mssssssss+
   /sssssssssss\033[0;37mhdmNNNNmyNMMMMh\033[0;34mssssss/
    .ossssssssssssssssss\033[0;37mdMMMNy\033[0;34msssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.""",
            f"""\033[0;31m
            .-/+oossssoo+/-.               {username}@linux
        `:+ssssssssssssssssss+:`           ----------------------
      -+ssssssssssssssssssyyssss+-         OS: \033[0;37mUbuntu Terminal\033[0;31m
    .ossssssssssssssssss\033[0;37mdMMMNy\033[0;31msssso.       Kernel: \033[0;37m</AL7>\033[0;31m
   /sssssssssss\033[0;37mhdmmNNmmyNMMMMh\033[0;31mssssss/
  +sssssssss\033[0;37mhm\033[0;31myd\033[0;37mMMMMMMMNddddy\033[0;31mssssssss+     Shell: \033[0;37mbash & Python 3\033[0;31m
 /ssssssss\033[0;37mhNMMM\033[0;31myh\033[0;37mhyyyyhmNMMMNh\033[0;31mssssssss/    Terminal: \033[0;37mGnom\033[0;31m
.ssssssss\033[0;37mdMMMNh\033[0;31mssssssssss\033[0;37mhNMMMd\033[0;31mssssssss.   
+ssss\033[0;37mhhhyNMMNy\033[0;31mssssssssssss\033[0;37myNMMMy\033[0;31msssssss+   
oss\033[0;37myNMMMNyMMh\033[0;31mssssssssssssss\033[0;37mhmmmh\033[0;31mssssssso 
oss\033[0;37myNMMMNyMMh\033[0;31mssssssssssssssmhmmmh\033[0;31mssssssso
+ssss\033[0;37mhhhyNMMNy\033[0;31mssssssssssss\033[0;37myNMMMy\033[0;31msssssss+
.ssssssss\033[0;37mdMMMNh\033[0;31mssssssssss\033[0;37mhNMMMd\033[0;31mssssssss.
 /ssssssss\033[0;37mhNMMM\033[0;31myh\033[0;37mhyyyyhdNMMMNh\033[0;31mssssssss/
  +sssssssss\033[0;37mdm\033[0;31myd\033[0;37mMMMMMMMMddddy\033[0;31mssssssss+
   /sssssssssss\033[0;37mhdmNNNNmyNMMMMh\033[0;31mssssss/
    .ossssssssssssssssss\033[0;37mdMMMNy\033[0;31msssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-."""]
        print(random.choice(a))
def history():
        if command=="history":
            file=open('history.txt','r')
            a=file.read()
            print(a)
def reboot():
        if command=="reboot":
            q=input("do you want off the computer? [y/n] ")
            if q.lower()=="y" or q.lower()=="yes":
                os.system("shutdown /s")
            if q.lower()=="n" or q.lower()=="no":
                print("EXIT...")
def ls():
        if command=="ls":
            os.system("dir")
def mkdir():
        if "mkdir " in command:
            os.system(f"{command}")
def rm():
        if "rm " in command:
            a=command.replace('rm ','rd /S ')
            os.system(a)
                
def clear():
        if command=="clear":
            os.system("cls")
def copy():
        if "cp " in command:
            a=command.replace('cp ','copy ')
            os.system(a)
def pwd():
        if command=="pwd":
            os.system("cd")
def cat():
        if "cat " in command:
            a=command.replace('cat ','')
            file=open(a,'r')
            read=file.read()
            print(read)
def exit1():
        if command.lower()=="exit":
            exit("Thanks for use terminal")
def python():
        if command=="python":
            os.system("python")
def pip_install():
        if "pip install" in command:
            os.system(command)
def pip3_install():
        if "pip3 install" in command:
            os.system(command)
def python3():
        if "python3" in command:
            if ".py" in command:
                os.system(command)
def creat_file():
        if "touch" in command:
            a=command.replace("touch",'')
            file=open(a,"w")
            file.write(" ")
            file.close()
def nano():
        if "nano" in command:
            os.system("cls")
            q=command.replace("nano",'')
            file=open(q,"w")
            while True:
                a=input("")
                
                if a=="^x" or a=="^X":
                    break
                else:
                    file=open(q,"a")
                    file.write("\n"+a)
                    file.close()
            file.close() 
def bash():
        if "echo" in command:
            os.system(command)         
def ifconfig():
        if command=="ifconfig":
            os.system("ipconfig")
def mv():
        if "mv " in command:
            a=command.replace("mv ","ren ")
            os.system(a)
def open1():
        if command=="notepad":
            os.system('notepad')
        elif command=="calc":
            os.system("calc")
def nmap():
        if "nmap " in command:
            a=command.replace('nmap ','')
            import socket
            ip = a
            s = socket.socket(2, 1) #socket.AF_INET, socket.SOCK_STREAM

            def porttry(ip, port):
                try:
                    s.connect((ip, port))
                    return True
                except:
                    return None

            for port in range(70, 101):
                value = porttry(ip, port)
                if value == None:
                    print("Port not opened %d" % port)
                else:
                    print("Port opened %d" % port)
def sublime():
        if command=="sublime_text3" or command=="sublime":
            subprocess.call("Sublime Text 3\sublime_text.exe")
def one_zero():
        if command.lower()=="1,0 to en" or command.lower()=="en to 1,0":
            subprocess.call("python3 1,0.py")
def date():
    if command=="date":
        print(time.ctime())
def hash():
        if " | md5" in command:
            a=command.replace(' | md5','')
            md5_hash=md5(a.encode()).hexdigest()
            print(md5_hash)
        #base64
        elif " | base64" in command:
            a=command.replace(' | base64','')
            base=a.encode('utf-8')
            try:
                base64_decode=base64.decodebytes(base)
                print(base64_decode.decode('utf-8'))
            except:
                base64_=base64.b64encode(base)
                print(base64_.decode('utf-8'))
        #base32
        elif " | base32" in command:
            a=command.replace(' | base32','')
            base=a.encode('utf-8')
            base32_=base64.b32encode(base)
            print(base32_.decode('utf-8'))
                
#kali_linux theme
while theme=="1":
    command=input(f"""
\033[0;34m┌──(\033[0;31mhassan@linux\033[0;34m)-[\033[0;40m~\033[0;34m]
└─\033[0;31m# \033[0;40m""")
    date()
    hash()
    one_zero()
    neofetch_kali()
    reboot()
    history()
    cat()
    sublime()
    nmap()
    mv()
    open1()
    ifconfig()            
    bash()
    nano()
    creat_file()            
    python3()
    pip3_install()
    pip_install()
    python()
    pwd()
    rm()
    copy()
    exit1()
    clear()
    mkdir()        
    ls()


#ubuntu theme
while theme=="2":
    print("""""")
    command=input(f"\033[0;32m{username}@linux\033[0;37m:\033[0;34m~\033[0;37m$ ")
    date()
    hash()
    one_zero()
    neofetch_ubuntu()
    reboot()
    history()
    cat()
    sublime()
    nmap()
    mv()
    open1()
    ifconfig()            
    bash()
    nano()
    creat_file()            
    python3()
    pip3_install()
    pip_install()
    python()
    pwd()
    rm()
    copy()
    exit1()
    clear()
    mkdir()        
    ls()
#AL7 theme
while theme=="3":
    print("""""""")
    command=input(f"""
\033[0;35m{username}@linux \033[0;37m[\033[0;34m~/Terminal\033[0;37m]\033[3;34m$ \033[0;37m""")
    history_file=open("history.txt",'a')
    history_file.write(command+"\n")
    history_file.close()
    #import def
    date()
    hash()
    one_zero()
    neofetch_AL7()
    reboot()
    history()
    cat()
    sublime()
    nmap()
    mv()
    open1()
    ifconfig()            
    bash()
    nano()
    creat_file()            
    python3()
    pip3_install()
    pip_install()
    python()
    pwd()
    rm()
    copy()
    exit1()
    clear()
    mkdir()        
    ls()
