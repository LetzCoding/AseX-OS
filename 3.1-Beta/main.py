import platform
import random
import sys
import time
import os
import datetime
from datetime import datetime
import vos as vo
try: 
    from cefpython3 import cefpython as cef
except:
    print("WARNING: No module named \"cefpython3\".")
with open(r"./Data/login.ax", 'r') as f:
    Login = f.read()
with open(r"./Data/username.ax", 'r') as f:
    Username = f.read()
with open(r"./Data/ins_vos.ax", 'r') as f:
    ins_vos = f.read()
with open(r"./Data/ins_bro.ax", 'r') as f:
    ins_bro = f.read()
with open(r"./Data/ins_doc.ax", 'r') as f:
    ins_doc = f.read()
with open(r"./Data/ins_ser.ax", 'r') as f:
    ins_ser = f.read()
with open(r"./Data/subShell.ax","r") as f:
    subShell=f.read()
dire="/"
class filestuff():
    def newfile(arg):
        if not arg:
            fileName = input('Filename $ ')
        else:
            fileName=arg
        if (fileName == ''):
            print("Error/Filename error")
        else:
            print('Creating......')
            try:
                newFile = open(str(dire)+"/"+str(fileName), "w")
            except:
                print("Error/File error")
                return 127
            print("Enter your file content until you press EOF. ^C to write a \\b.")
            aaa=1
            while aaa==1:
                try:
                    fileContent = input('Type $ ')
                    newFile.write(str(fileContent)+"\n")
                except EOFError: aaa=0
                except KeyboardInterrupt:
                    print()
                    newFile.write("\b")
            print('\nFile saved')
            newFile.close()
    def openfile(arg):
        try:
            if not arg:
                fileName = input('Filename $ ')
            else:
                fileName=arg
            seeFile = open(str(dire)+"/"+str(fileName), "r")
            text = seeFile.read()
            seeFile.close()
            print(text)
        except FileNotFoundError:
            print('[ Filename_info ] > Error/openFile error')
    def removefile(arg):
        try:
            if not arg:
                fileName=input("Input file $ ")
            else:
                fileName=arg
            tf=input("Really remove file "+str(fileName)+" ? [Y/n]")
            if tf=="y" or tf=="Y":
                os.system("rm -rf "+str(dire)+str(fileName))
            else:
                return 0
        except FileNotFoundError:
            print("[ Filename_info ] > Error/File not found error")
    def cd(arg):
        if not arg:
            direc=input("Directory $ ")
            print("Number error!")
            direc=str(direc)
            try:
                if(direc[0]=='/'): return direc
                elif(direc==".."): return qdir
                elif(direc=="."): return dire
                else: return dire+"/"+direc
            except:
                print("[ Input_info ] > Error/Input error")
        else:
            direc=arg
            direc=str(direc)
            if(direc[0]=='/'): return direc
            elif(direc==".."): return qdir
            elif(direc=="."): return dire
            else: return dire+"/"+direc
    def ls(arg):
        if not arg:
            os.system("ls -lspAh "+str(dire))
        else:
            os.system("ls -lspAh "+str(arg))
    def mkdir(arg):
        if not arg:
            direc=input("Directory $ ")
            os.system("mkdir "+str(dire)+"/"+str(direc))
        else:
            os.system("mkdir "+str(dire)+"/"+str(arg))

class util():
    version="AseX-OS 3.1 -- FileOp"
    def clear():
        os.system("clear")
    def timer(arg):
        if not arg:
            try: inputTime=float(input("Time $ "))
            except: print("[ Utilities -- timer ] > Error/Input error")
        else:
            try: inputTime=float(arg)
            except: print("[ Utilities -- timer ] > Error/Input error")
        try:
            time.sleep(inputTime)
        except:
            print("[ Utilities -- timer ] > Error/Input error")
        print("Done.\a")
    def setSubShell(arg):
        if not arg:
            newSubShell=str(input("New Sub-Shell $ "))
        else:
            newSubShell=str(arg)
        f=open("./Data/subShell.ax","w")
        f.write(newSubShell)
        f.close()
        print("You need to restart AseX-OS.")
class acmd():
    def ver():
        print("&   &  AseX-OS Oprating System - FileOp")
        time.sleep(0.05)
        print(" & &   Aser inc. ©2021 All right reserved")
        time.sleep(0.05)
        print("  &    AseX kernel 4.1 Copyright ©2021")
        time.sleep(0.05)
        print(" & &   AseX-OS OS Version:3.1.Beta - FileOp")
        time.sleep(0.05)
        print("&   &  Codename : FileOp")
        time.sleep(0.05)
        print("\nMade by pntang, 2021.")
        time.sleep(0.05)
        print("Autorized to Hangco.")
    def setlogin():
        newl = input('SetLog $ ')
        with open(r"./Data/login.ax", "w") as f:
            f.write(newl)
        print('[ Set Log_info ] > Please restart to change your login')
    def setusrnm():
        newu = input('SetUsername $ ')
        with open(r"./Data/username.ax", "w") as f:
            f.write(newu)
        print('[ Set Username_info ] > Please restart to change your Username')
    def time():
        print(datetime.now())
    def shell():
        if subShell=="":
            print("AseX-OS shell 15.0")
            while True:
                shell = input(" $ ")
                if shell == 'platform':
                    print(" ", sys.platform)
                elif shell == 'version':
                    print(" ", sys.version)
                elif shell == 'copyright':
                    print(" ", sys.copyright)
                elif shell == 'time':
                    print(" ", datetime.now())
                elif shell == 'run':
                    srun = input(" $ run ")
                    os.system(srun)
                elif shell == 'cmd':
                    os.system('bash')
                elif shell == 'python':
                    os.system('python3')
                elif shell == 'exit':
                    break
                elif shell == '':
                    continue
                else:
                    print("Error command")
        else:
            os.system(str(subShell))
class aapp():
    def vos(): vo.main()
    def ssp():
        print('Standard Software Pack')
        time.sleep(0.3)
        print('Type ins_<application>/uni_<application> to install/uninstall software')
        time.sleep(0.1)
        while True:
            ssp = input(' Software Pack $ ')
            if ssp == 'help':
                print('SSP/ssp_list - ins_vos/uni_vos / Install/Uninstall Virtual OS')
                time.sleep(0.05)
                print('SSP/ssp_list - ins_bro/uni_bro / Install/Uninstall Browser')
                time.sleep(0.05)
                print('SSP/ssp_list - ins_doc/uni_doc / Install/Uninstall PyDocx')
                time.sleep(0.05)
                print('SSP/ssp_list - ins_ser/uni_ser / Install/Uninstall Http_server')
            elif ssp == 'ins_vos':
                print('Intalling...')
                with open(r"./Data/ins_vos.ax", "w") as f:
                    f.write('True')
                time.sleep(3)
                print('Installing completed')
            elif ssp == 'uni_vos':
                print('Uninstalling')
                with open(r"./Data/ins_vos.ax", "w") as f:
                    f.write('False')
                time.sleep(3)
                print('Uninstalling completed')
            elif ssp == 'ins_bro':
                print('Intalling...')
                with open(r"./Data/ins_bro.ax", "w") as f:
                    f.write('True')
                time.sleep(3)
                print('Installing completed')
            elif ssp == 'uni_bro':
                print('Uninstalling')
                with open(r"./Data/ins_vos.ax", "w") as f:
                    f.write('False')
                time.sleep(3)
                print('Uninstalling completed')
            elif ssp == 'ins_doc':
                print('Intalling...')
                with open(r"./Data/ins_doc.ax", "w") as f:
                    f.write('True')
                time.sleep(3)
                print('Installing completed')
            elif ssp == 'uni_doc':
                print('Uninstalling')
                with open(r"./Data/ins_doc.ax", "w") as f:
                    f.write('False')
                time.sleep(3)
                print('Uninstalling completed')
            elif ssp == 'ins_ser':
                print('Intalling...')
                with open(r"./Data/ins_ser.ax", "w") as f:
                    f.write('True')
                time.sleep(3)
                print('Installing completed')
            elif ssp == 'uni_ser':
                print('Uninstalling')
                with open(r"./Data/ins_vos.ax", "w") as f:
                    f.write('False')
                time.sleep(3)
                print('Uninstalling completed')
            elif ssp == 'exit':
                break
            else:
                print("[ SSP_info ] > Cannot find '", ssp, "'")
    def bro():
        try: from cefpython3 import cefpython as cef
        except: print("No module named \"cefpython3\", exit bro()."); return 1
        sys.excepthook = cef.ExceptHook
        cef.Initialize()
        new = input('Enter_URL $ ')
        if new == '':
            web = 'https://sprinkleguide.github.io/index.html'
        else:
            web = new
        cef.CreateBrowserSync(url=web, window_title="AseX-OS Browser 1.1.13")
        cef.MessageLoop()
        cef.Shutdown()
    def doc():
        from docx import Document
        document = Document()
        print("Pydocx")
        while True:
            doc = input(' |')
            if doc == '/exit':
                break
            elif doc == '/save':
                print('New.docx saved')
                document.save("new.docx")
            else:
                document.add_paragraph(doc)
    def ser():
        os.system("python3 -m http.server 1111")

if Login == 'admin':
    Login = 'admin'
elif Login == 'root':
    Login = 'root'
else:
    Login = 'user'
print(" ")
print('AseX-OS - Core 1 ©2021 All right reserved')
time.sleep(0.3)
print("Type 'cmdlist' for Commandlist")
time.sleep(0.1)
qdir="/"
while True:
    dire=str(dire)
    qdir=str(dire)
    commandlist = input(dire + " " + Login + '@' + Username + '$ ')
    commands=commandlist.split()
    try:
        command=commands[0]; 
    except:
        command=""
    try: arg=commands[1]
    except: arg=None
    time.sleep(0.05)
    print("Called "+str(command)+" with arg "+str(arg)+".")
    if command == 'cmdlist':
        print('AseX-OS/Commandlist - cmdlist/Show command list')
        time.sleep(0.05)
        print('AseX-OS/Commandlist - applist/Show all apps')
        time.sleep(0.05)
        print("AseX-OS/Commandlist - setSubShell/Set Sub shell")
        time.sleep(0.05)
        print('AseX-OS/Commandlist - shell/Sub shell')
        time.sleep(0.05)
        print('AseX-OS/Commandlist - newfile/Create a new file')
        time.sleep(0.05)
        print('AseX-OS/Commandlist - openfile/Open a file')
        time.sleep(0.05)
        print("AseX-OS/Commandlist - removefile/Remove a file or a directory")
        time.sleep(0.05)
        print("AseX-OS/Commandlist - mkdir/Make a directory")
        time.sleep(0.05)
        print("AseX-OS/Commandlist - ls/list directory's stuff")
        time.sleep(0.05)
        print("AseX-OS/Commandlist - cd/Change directory")
        time.sleep(0.05)
        print('AseX-OS/Commandlist - time/Print datetime')
        time.sleep(0.05)
        print('AseX-OS/Commandlist - ver/Output version')
        time.sleep(0.05)
        print('AseX-OS/Commandlist - setlogin/set AseX-OS OS login')
        time.sleep(0.05)
        print('AseX-OS/Commandlist - setusrnm/set AseX-OS OS UserName')
        time.sleep(0.05)
        print("AseX-OS/Commandlist - timer/timer utility")
        time.sleep(0.05)
        print("AseX-OS/Commandlist - clear/clear screen")
        time.sleep(0.05)
        print('AseX-OS/Commandlist - exit/Exit AseX-OS OS')
    elif command == 'newfile':
        filestuff.newfile(arg)
    elif command == 'openfile':
        filestuff.openfile(arg)
    elif command == 'ver':
        acmd.ver()
    elif command == 'setlogin':
        acmd.setlogin()
    elif command == 'setusrnm':
        acmd.setusrnm()
    elif command == 'time':
        acmd.time()
    elif command=="removefile":
        filestuff.removefile(arg)
    elif command=="ls": filestuff.ls(arg)
    elif command=="cd": dire=filestuff.cd(arg)
    elif command=="mkdir": filestuff.mkdir(arg)
    elif command == 'applist':
        print("AseX-OS/Applist - ssp/Standard Software Pack")
        time.sleep(0.05)
        if ins_vos == 'True':
            print("AseX-OS/Applist - vos/AseX-OS Virtual OS")
        time.sleep(0.05)
        if ins_bro == 'True':
            print("AseX-OS/Applist - browser/AseX-OS Browser")
        time.sleep(0.05)
        if ins_doc == 'True':
            print("AseX-OS/Applist - docx/Write Docx")
        time.sleep(0.05)
        if ins_ser == 'True':
            print("AseX-OS/Applist - server/Run httpserver")
    elif command == 'server' and ins_ser == 'True':
        aapp.ser()
    elif command == 'ssp':
        aapp.ssp()
    elif command == "vos" and ins_vos == 'True':
        aapp.vos()
    elif command == 'browser' and ins_bro == 'True':
        aapp.bro()
    elif command == 'shell' and Login != 'User':
        acmd.shell()
    elif command == 'docx' and ins_doc == 'True':
        aapp.doc()
    elif command=="timer":
        util.timer(arg)
    elif command=="clear":
        util.clear()
    elif command=="setSubShell":
        util.setSubShell(arg)
    elif command == '':
        continue
    elif command == 'exit':
        print('AseX-OS is Shutting Down...')
        break
    else:
        print("[ AseX-OS_CMD_info ] > Error/Command_error: Cannot find '", command, "' command")
