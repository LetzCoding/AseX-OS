import time
import os
def main():
        print(" >AseX Virtual OS ©2021 All right reserved")
        time.sleep(1)
        while True:
            vs = input(" VirtualOS $ ")
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
                        print(" ver > Code Oprating System ©2021 All right reserved")
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
                loados = input(" LoadOS Disk $ ")
                os.system("python3 "+loados)
            elif vs == "exit":
                break
            elif vs == "help":
                print(" HelpList")
                time.sleep(0.05)
                print(" |CodeOS > Run CodeOS locally")
                time.sleep(0.05)
                print(" |loados > Load OS Disk")
                time.sleep(0.05)
                print(" |exit > Quit Vitual System")
            elif vs == "":
                continue
            else:
                print(" Error Vitual System command")
