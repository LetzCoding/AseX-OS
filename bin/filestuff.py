from datetime import datetime
import datetime
import os
import time
import sys
import random
import platform


class filestuff():
    def newfile(arg):
        if not arg:
            fileName = input('Filename $ ')
        else:
            fileName = arg
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
            aaa = 1
            while aaa == 1:
                try:
                    fileContent = input('Type $ ')
                    newFile.write(str(fileContent)+"\n")
                except EOFError:
                    aaa = 0
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
                fileName = arg
            seeFile = open(str(dire)+"/"+str(fileName), "r")
            text = seeFile.read()
            seeFile.close()
            print(text)
        except FileNotFoundError:
            print('[ Filename_info ] > Error/openFile error')

    def removefile(arg):
        try:
            if not arg:
                fileName = input("Input file $ ")
            else:
                fileName = arg
            tf = input("Really remove file "+str(fileName)+" ? [Y/n]")
            if tf == "y" or tf == "Y":
                os.system("rm -rf "+str(dire)+str(fileName))
            else:
                return 0
        except FileNotFoundError:
            print("[ Filename_info ] > Error/File not found error")

    def cd(arg):
        if not arg:
            direc = input("Directory $ ")
            direc = str(direc)
            try:
                if(direc[0] == '/'):
                    return direc
                elif(direc == ".."):
                    return qdir
                elif(direc == "."):
                    return dire
                else:
                    return dire+"/"+direc
            except:
                print("[ Input_info ] > Error/Input error")
        else:
            direc = arg
            direc = str(direc)
            if(direc[0] == '/'):
                return direc
            elif(direc == ".."):
                return qdir
            elif(direc == "."):
                return dire
            else:
                return dire+"/"+direc

    def ls(arg):
        t = arg
        if not arg:
            t = dire
        if osname == "posix":
            os.system("ls -lspAh "+str(t))
        elif osname == "nt":
            os.system("dir "+str(t))
        else:
            print("OS Name Error")

    def mkdir(arg):
        if not arg:
            direc = input("Directory $ ")
            os.system("mkdir "+str(dire)+"/"+str(direc))
        else:
            os.system("mkdir "+str(dire)+"/"+str(arg))
