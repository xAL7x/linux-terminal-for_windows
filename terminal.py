import os
import time
import subprocess
try:
    import ascii_magic
    import pyfiglet
    
except:
    os.system("pip install ascii_magic")
    os.system("pip install pyfiglet")
os.system("cls")
time.sleep(2)
qwer=("kali1.png")
out=ascii_magic.from_image_file(qwer,columns=150,char=']')
ascii_magic.to_terminal(out)
time.sleep(2)
os.system("cls")
pyfiglet.print_figlet("Linux")
print("============> Created by alhassanAlharb7 <============")
username=input("User name: ")

while True:
    print("_"*60)
    command=input(f"""
\033[0;32m┌──(\033[0;34m{username}@linux\033[0;32m)-[\033[0;40m~\033[0;32m]
└─\033[0;34m$ \033[0;40m""")
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

            s=""
            t=""
            for i in range(len(command)):
                if (i!=1):
                    t+=command[i]
            for i in range(len(t)):
                if (i!=0):
                    s+=t[i]
            os.system("copy"+s)
    def pwd():
        if command=="pwd":
            os.system("cd")
    def exit1():
        if command=="exit":
            exit()
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
            file.write('')
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

            for port in range(78, 84):
                value = porttry(ip, port)
                if value == None:
                    print("Port not opened %d" % port)
                else:
                    print("Port opened %d" % port)
                    break
    def sublime():
        if command=="sublime_text3" or command=="sublime":
            subprocess.call("Sublime Text 3\sublime_text.exe")
    def open_git_bash():
        if command=="open git bash" or command=="open git Bash" or command=="git bash" or command=="git Bash":
            subprocess.call("Git\git-bash.exe")
    #import def
    open_git_bash()
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
#_________________________________________________
#______________________________________
    if command=="sudo":
        while True:
            print("_"*60)   
            command=input(f"""
\033[0;34m┌──(\033[0;31m{username}💀linux\033[0;34m)-[\033[0;40m~\033[0;34m]
└─\033[0;31m# \033[0;40m""")
            open_git_bash()
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