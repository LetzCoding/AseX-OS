from datetime import datetime
import datetime
import os
import time
import sys
import random
import platform


class settings():
    def main():
        setstuff = input(
            "Welcome to Settings. Please input a number in 1, 2 and 3. We'll use this number to do a setting work.\n(1: set sub shell; 2: set login; 3: set username.)\n[ settings ] $ ")
        if setstuff == "1":
            newSubShell = str(input("New Sub-Shell $ "))
            with open(r"./Data/subShell.ax", "w") as f:
                f.write(newSubShell)
            print("You'll have to restart AseX-OS.")
        elif setstuff == "2":
            newl = input('SetLog $ ')
            with open(r"./Data/login.ax", "w") as f:
                f.write(newl)
            print('[ Set Log_info ] > Please restart to change your login')
        elif setstuff == "3":
            newu = input('SetUsername $ ')
            with open(r"./Data/username.ax", "w") as f:
                f.write(newu)
                print(
                    '[ Set Username_info ] > Please restart to change your Username')
        else:
            print("Invalid option!")



