print("Starting AseX-OS...")
start_info = '''
╭━━━╮╱╱╱╱╱╱╱╱╭━╮╭━╮╱╱╱╱╭━━━╮╭━━━╮
┃╭━╮┃╱╱╱╱╱╱╱╱╰╮╰╯╭╯╱╱╱╱┃╭━╮┃┃╭━╮┃
┃┃╱┃┃╭━━╮╭━━╮╱╰╮╭╯╱╱╱╱╱┃┃╱┃┃┃╰━━╮
┃╰━╯┃┃━━┫┃┃━┫╱╭╯╰╮╱╭━━╮┃┃╱┃┃╰━━╮┃
┃╭━╮┃┣━━┃┃┃━┫╭╯╭╮╰╮╰━━╯┃╰━╯┃┃╰━╯┃
╰╯╱╰╯╰━━╯╰━━╯╰━╯╰━╯╱╱╱╱╰━━━╯╰━━━╯
'''
import platform
print("imported platfrom")
import random
print("imported random")
import sys
print("imported sys")
import time
print("imported time")
import os
print("imported os")
import datetime
print("imported datetime")
from datetime import datetime
print("imported datetime from datetime")
import vos as vo
print("imported vos as vo")
try:
    print("starting to load file...")
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
    print("loaded login, uername, ins_*, subShell")
    print("setting variables...")
    dire="/"
    osname=os.name
    print("setting variables completed")
except:
    print("Fail: Load Error")
    time.sleep(0.05)
    print('Please Goto "https://github.com/letzcoding/asex-os to download newest edition."')
    exit(1)
from filestuff import filestuff
print("loaded filestuff class")
from util import util
print("loaded util class")
from settings import settings
from acmd import acmd
print("Loaded Ase-X Cmd class")
from aapp import aapp
print("Loaded Ase-X App class")
if Login == 'admin':
    Login = 'admin'
elif Login == 'root':
    Login = 'root'
else:
    Login = 'user'
print("loaded users")
print("[System - info] > Load Completed, Starting Ase-X OS\n\n")
time.sleep(1)
print(start_info)
# print('\n\n\nAseX-OS - 3.2 LetzCoding 2022 © All Right Reserved')
time.sleep(0.3)
print("Type 'cmdlist' for Commandlist")
time.sleep(0.1)
qdir="/"
try:
    while True:
        dire=str(dire)
        qdir=str(dire)
        commandlist = input(Login + '@' + Username + '/' + dire + '$ ')
        commands = commandlist.split()
        try:
            command=commands[0]; 
        except:
            command=""
        try:
            arg=commands[1]
        except:
            arg=None
        time.sleep(0.05)
        print("Called "+str(command)+" with arg "+str(arg)+".")
        if command == 'cmdlist':
            print('AseX-OS/Commandlist - cmdlist/Show command list')
            time.sleep(0.05)
            print('AseX-OS/Commandlist - applist/Show all apps')
            time.sleep(0.05)
            print('AseX-OS/Commandlist - newfile/Create a new file')
            time.sleep(0.05)
            print('AseX-OS/Commandlist - openfile/Open a file')
            time.sleep(0.05)
            print("AseX-OS/Commandlist - removefile/Remove a file or a directory")
            time.sleep(0.05)
            print('AseX-OS/Commandlist - time/Print datetime')
            time.sleep(0.05)
            print('AseX-OS/Commandlist - ver/Output version')
            time.sleep(0.05)
            print("AseX-OS/Commandlist - timer/timer utility")
            time.sleep(0.05)
            print("AseX-OS/Commandlist - clear/clear screen")
            time.sleep(0.05)
            print("AseX-OS/Commandlist - settings/set some stuff")
            time.sleep(0.05)
            print('AseX-OS/Commandlist - exit/Exit AseX-OS OS')
        elif command == 'newfile':
            filestuff.newfile(arg)
        elif command == 'openfile':
            filestuff.openfile(arg)
        elif command == 'ver':
            acmd.ver()
        elif command == "settings":
            settings.main()
        elif command == 'time':
            acmd.time()
        elif command=="removefile":
            filestuff.removefile(arg)
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
        elif command == 'docx' and ins_doc == 'True':
            aapp.doc()
        elif command=="timer":
            util.timer(arg)
        elif command=="clear":
            util.clear()
        elif command == '':
            continue
        elif command == 'exit':
            print('AseX-OS is Shutting Down...')
            exit(1)
        else:
            os.system(command)
except EOFError:
    print("\nEOF, exiting...")
    exit(1)
except KeyboardInterrupt:
    print("\n^C, exiting...")
    exit(1)
