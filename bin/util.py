from datetime import datetime
import datetime
import os
import time
import sys
import random
import platform


class util():
    version = "AseX-OS 3.1 Beta SP1 -- FileOp"

    def clear():
        if osname == "posix":
            os.system("clear")
        else:
            os.system("cls")

    def timer(arg):
        if not arg:
            try:
                inputTime = float(input("Time $ "))
            except:
                print("[ Utilities - timer ] > Error/Input error")
        else:
            try:
                inputTime = float(arg)
            except:
                print("[ Utilities - timer ] > Error/Input error")
        try:
            time.sleep(inputTime)
        except:
            print("[ Utilities - timer ] > Error/Input error")
        print("Done.\a")
