from datetime import datetime
import datetime
import os
import time
import sys
import random
import platform


class aapp():
    def vos():
        vo.main()
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
                print('SSP/ssp_list - else / Download App From "LetzCoding.github.io/software"')
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
                try:
                    import requests
                    mirror = "https://LetzCoding.github.io/software/"
                    r = requests.get(mirror + 'ssp')
                except:
                    print("[ SSP - WARNING ]> No module named 'requests'")

    def bro():
        try:
            import cefpython3
            sys.excepthook = cef.ExceptHook
            cef.Initialize()
            new = input('Enter_URL $ ')
            if new == '':
                web = 'https://cn.bing.com/'
            else:
                web = new
            cef.CreateBrowserSync(
                url=web, window_title="AseX-OS Browser 1.1.13")
            cef.MessageLoop()
            cef.Shutdown()
        except:
            print("[ Browser - WARNING ]> No module named 'cefpython3'")

    def doc():
        try:
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
        except:
            print("[ docx - WARNING ]> No module named 'py-docx'")

    def ser():
        os.system("python3 -m http.server 1111")
