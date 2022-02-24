# AseX OS API
class fileMan():
    ## Funcs api_editFile*:
    # These funcs are used to edit a writable file.
    # Please use the `w', `a' or `r+' file var to use this func.
    def api_editFile(filename):
        try:
            aaa=1
            while aaa==1:
                try:
                    fileContent = input('Content> ')
                    filename.write(str(fileContent)+"\n")
                except EOFError: aaa=0
                except KeyboardInterrupt:
                    print()
                    filename.write("\b")
            filename.close()
            return 0
        except:
            return 1
    def api_editFile_info():
        return "Enter your file content until you press EOF. ^C to write a \\b."

    ## Funcs api_readFile*:
    # These funcs are used to read a file.
    # Please use the `r*' file var to use this func.
    def api_readFile(filename):
        try:
            f=open(filename)
            content=f.read()
            print(content)
            f.close()
            return 0
        except:
            return 1
