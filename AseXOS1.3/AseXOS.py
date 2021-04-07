import platform
import sys
import time
import os
import datetime
from datetime import datetime

print("Launching BIOS...")
time.sleep(1)
print("Launching System...")
time.sleep(1)
with open(r".\Data\log.ax", 'r') as f:
    Login = f.read()
with open(r".\Data\ins_gp.ax", 'r') as f:
    gp = f.read()
with open(r".\Data\ins_vos.ax", 'r') as f:
    ins_vos = f.read()
with open(r".\Data\ins_bro.ax", 'r') as f:
    ins_bro = f.read()
with open(r".\Data\ins_doc.ax", 'r') as f:
    ins_doc = f.read()
with open(r".\Data\ins_ser.ax", 'r') as f:
    ins_ser = f.read()
with open(r".\Data\gpa.ax", 'r') as f:
    gpa = f.read()
with open(r".\Data\gpm.ax", 'r') as f:
    gpm = f.read()
if Login == 'Admin':
    Login = 'Admin'
elif Login == '0x1010010001':
    Login = 'root'
else:
    Login = 'User'
print(" ")
print('AseX Oprating System - Core ©2020 All right reserved')
time.sleep(0.3)
print("Type 'cmdlist' for Commandlist")
time.sleep(0.1)
while True:
    command = input('[ Login-'+Login+' ] > ')
    if command == 'cmdlist':
        print('AseX/Command1list - cmdlist\Show command list')
        time.sleep(0.05)
        print('AseX/Command2list - applist\Show all apps')
        time.sleep(0.05)
        print('AseX/Command3list - shell\AseX shell')
        time.sleep(0.05)
        print('AseX/Command4list - newfile\Create a new file')
        time.sleep(0.05)
        print('AseX/Command5list - openfile\Open a file')
        time.sleep(0.05)
        print('AseX/Command6list - time\Print datetime')
        time.sleep(0.05)
        print('AseX/Command7list - ver\Output version')
        time.sleep(0.05)
        print('AseX/Command8list - setlog\set AseX OS log')
        time.sleep(0.05)
        print('AseX/Command9list - exit\Exit AseX OS')
    elif command == 'newfile':
        fileName = input('[ Filename ] > ')
        if (fileName == ''):
            print("Error/Filename error")
            continue
        else:
            print('Creating......')
            newFile = open(fileName, "w")
            fileContent = input('[ Type ] > ')
            newFile.write(fileContent)
            print('File saved')
            newFile.close()
    elif command == 'openfile':
        try:
            fileName = input('[ Filename ] > ')
            seeFile = open(fileName, "r")
            text = seeFile.readline()
            seeFile.close()
            print('Openfile:', text)
        except:
            print('[ Filename ] > Error/openFile error')
            continue
    elif command == 'ver':
        print("&   &  AseX Oprating System - Core")
        time.sleep(0.05)
        print(" & &   Aser inc. ©2021 All right reserved")
        time.sleep(0.05)
        print("  &    AseX kernel 2.0 Copyright ©2021")
        time.sleep(0.05)
        print(" & &   AseX OS Version:1.2 - Core")
        time.sleep(0.05)
        print("&   &  Login:", Login)
    elif command == 'setlog':
        newl = input('[ SetLog ] > ')
        with open(r".\Data\log.ax", "w") as f:
            f.write(newl)
        print('[ Set Log ] > Please restart to change your log')
    elif command == 'exit':
        print('Closing...')
        time.sleep(0.5)
        break
    elif command == 'time':
        print(datetime.now())
    elif command == 'applist':
        print("AseX/Applist - ssp\Standard Software Pack")
        time.sleep(0.05)
        if ins_vos == 'True':
            print("AseX/Applist - vos\AseX Virtual OS")
        time.sleep(0.05)
        if ins_bro == 'True':
            print("AseX/Applist - browser\AseX Browser")
        time.sleep(0.05)
        if ins_doc == 'True':
            print("AseX/Applist - docx\Write Docx")
        time.sleep(0.05)
        if ins_ser == 'True':
            print("AseX/Applist - server\Run httpserver")
        time.sleep(0.05)
        if gp == 'True':
            print("AseX/Applist - gp\GamePass")
    elif command == 'server' and ins_ser == 'True':
        os.system("python -m http.server 1111")
    elif command == 'ssp':
        print(' Standard Software Pack')
        time.sleep(0.3)
        print(' Type ins_<item>/uni_<items> to install/uninstall software')
        time.sleep(0.1)
        while True:
            ssp = input(' [ SSP ] > ')
            if ssp == 'help':
                print(' SSP/ssp_list - ins_gp/uni_gp \ Install/Uninstall GamePass')
                time.sleep(0.05)
                print(' SSP/ssp_list - ins_vos/uni_vos \ Install/Uninstall Virtual OS')
                time.sleep(0.05)
                print(' SSP/ssp_list - ins_bro/uni_bro \ Install/Uninstall Browser')
                time.sleep(0.05)
                print(' SSP/ssp_list - ins_doc/uni_doc \ Install/Uninstall PyDocx')
                time.sleep(0.05)
                print(' SSP/ssp_list - ins_ser/uni_ser \ Install/Uninstall Http_server')
            elif ssp == 'ins_gp':
                print(' Intalling...')
                with open(r".\Data\ins_gp.ax", "w") as f:
                    f.write('True')
                time.sleep(3)
                print(' Installing completed')
            elif ssp == 'uni_gp':
                print(' Uninstalling')
                with open(r".\Data\ins_gp.ax", "w") as f:
                    f.write('False')
                time.sleep(3)
                print(' Uninstalling completed')
            elif ssp == 'ins_vos':
                print(' Intalling...')
                with open(r".\Data\ins_vos.ax", "w") as f:
                    f.write('True')
                time.sleep(3)
                print(' Installing completed')
            elif ssp == 'uni_vos':
                print(' Uninstalling')
                with open(r".\Data\ins_vos.ax", "w") as f:
                    f.write('False')
                time.sleep(3)
                print(' Uninstalling completed')
            elif ssp == 'ins_bro':
                print(' Intalling...')
                with open(r".\Data\ins_bro.ax", "w") as f:
                    f.write('True')
                time.sleep(3)
                print(' Installing completed')
            elif ssp == 'uni_bro':
                print(' Uninstalling')
                with open(r".\Data\ins_vos.ax", "w") as f:
                    f.write('False')
                time.sleep(3)
                print(' Uninstalling completed')
            elif ssp == 'ins_doc':
                print(' Intalling...')
                with open(r".\Data\ins_doc.ax", "w") as f:
                    f.write('True')
                time.sleep(3)
                print(' Installing completed')
            elif ssp == 'uni_doc':
                print(' Uninstalling')
                with open(r".\Data\ins_doc.ax", "w") as f:
                    f.write('False')
                time.sleep(3)
                print(' Uninstalling completed')
            elif ssp == 'ins_ser':
                print(' Intalling...')
                with open(r".\Data\ins_ser.ax", "w") as f:
                    f.write('True')
                time.sleep(3)
                print(' Installing completed')
            elif ssp == 'uni_ser':
                print(' Uninstalling')
                with open(r".\Data\ins_vos.ax", "w") as f:
                    f.write('False')
                time.sleep(3)
                print(' Uninstalling completed')
            elif ssp == 'exit':
                break
            else:
                print(" [ SSP ] > Cannot find '", ssp, "'")
    elif command == "gp" and gp == "True":
        print(' GamePass 1.0 ©2021 AllRight Reserved')
        if gpa == "False":
            print(" [ GamePass ] > You haven't actived GamePass")
            gpain = input(' [ GamePass_Active - input Your Number ] > ')
            if gpain == 'gpa01-21314-1518-01':
                with open(r".\Data\gpa.ax", "w") as f:
                    f.write('True')
                print(' [ GamePass ] > GamePass Actived')
            else:
                print(' [ GamePass ] > GamePass UnActived')
        elif gpa == "True":
            while True:
                gpcmd = input(' [ GamePass ] > ')
                if gpcmd == 'unactive':
                    una = input('  [ GamePass ] > Press enter to unactive')
                    with open(r".\Data\gpa.ax", "w") as f:
                        f.write('False')
                elif gpcmd == 'help':
                    print(' GamePassCMD - unactive \ GamepassUnactive')
                    time.sleep(0.05)
                    print(' GamePassCMD - run \ Run GamePass_pygame')
                    time.sleep(0.05)
                    print(' GamePassCMD - member \ GamePass Member')
                    time.sleep(0.05)
                    print(' GamePassCMD - exit \ Exit GamePass')
                elif gpcmd == 'run':
                    import pygame
                elif gpcmd == 'member':
                    with open(r".\Data\gpm.ax", "w") as f:
                        f.write('True')
                elif gpcmd == 'exit':
                    break
                else:
                    print(' [ GamePass ] > Enter run to Launch GamePass')
    elif command == "vos" and ins_vos == 'True':
        print(" >AseX Virtual OS ©2020 All right reserved")
        time.sleep(1)
        while True:
            vs = input(" Virtual >")
            if vs == "CodeOS":
                print(" ")
                print(" Starting Virtual Machine...")
                time.sleep(1)
                print(" Installing BIOS...")
                time.sleep(1)
                print(" Installing System...")
                time.sleep(3)
                print(" ")
                print(" Code OS 5.0")
                time.sleep(0.05)
                print(" Type list for command list")
                while True:
                    cmd = input(" [ CodeOS ] > ")
                    if cmd == 'list':
                        print(" list > list/output command list")
                        time.sleep(0.05)
                        print(" list > ver/check Code OS version")
                        time.sleep(0.05)
                        print(" list > new/create a new file")
                        time.sleep(0.05)
                        print(" list > open/open a file")
                        time.sleep(0.05)
                        print(" list > time/check datetime")
                        time.sleep(0.05)
                        print(" list > logout/close Code OS")
                    elif cmd == 'ver':
                        print(" ver > Code Oprating System ©2020 All right reserved")
                        time.sleep(0.05)
                        print(" Copyright > Aser Technology.inc")
                        time.sleep(0.05)
                        print(" num > 2080-5084-70-021")
                    elif cmd == 'new':
                        fname = input(' Filename >')
                        if (fname == ''):
                            print(" error > Filename cannot be empty")
                            continue
                        else:
                            print(' >creating... ')
                            newf = open(fname, "w")
                            fc = input(' write >')
                            newf.write(fc)
                            print(' Done')
                            newf.close()
                    elif cmd == 'open':
                        try:
                            fname = input(' FileName >')
                            seef = open(fname, "r")
                            txt = seef.readline()
                            seef.close()
                            print(' File/', txt)
                        except:
                            print(' error > Cannot find the file')
                            continue
                    elif cmd == 'time':
                        print(' ', datetime.now())
                    elif cmd == 'logout':
                        print(" Closing...")
                        time.sleep(3)
                        break
                    elif cmd == '':
                        continue
                    else:
                        print(" error > Cannot find '", cmd, "'")
            elif vs == "loados":
                loados = input(" LoadOS Disk>")
                os.system(loados)
            elif vs == "importvm":
                import vm
            elif vs == "exit":
                break
            elif vs == "help":
                print(" HelpList")
                time.sleep(0.05)
                print(" |CodeOS > Run CodeOS locally")
                time.sleep(0.05)
                print(" |loados > Load OS Disk")
                time.sleep(0.05)
                print(" |importvm > Import vm.py")
                time.sleep(0.05)
                print(" |exit > Quit Vitual System")
            elif vs == "":
                continue
            else:
                print(" Error Vitual System command")
    elif command == 'browser' and ins_bro == 'True':
        from cefpython3 import cefpython as cef
        sys.excepthook = cef.ExceptHook
        cef.Initialize()
        new = input('[ Enter_URL ] > ')
        if new == '':
            web = 'https://sprinkleguide.github.io/index.html'
        else:
            web = new
        cef.CreateBrowserSync(url=web, window_title="AseX Browser")
        cef.MessageLoop()
        cef.Shutdown()
    elif command == 'shell' and Login != 'User':
        print(" AseX shell 15.0")
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
                os.system(shell)
            elif shell == 'python':
                os.system('python')
            elif shell == 'exit':
                break
            elif shell == '':
                continue
            else:
                print(" Error command")
    elif command == 'docx' and ins_doc == 'True':
        from docx import Document
        document = Document()
        print(" Pydocx")
        while True:
            doc = input(' |')
            if doc == '/exit':
                break
            elif doc == '/save':
                print(' New.docx saved')
                document.save("new.docx")
            else:
                document.add_paragraph(doc)

    elif command == '':
        continue
    else:
        print("[ AseX_CMD ] > Error/Command_error: Cannot find '", command, "' command")
