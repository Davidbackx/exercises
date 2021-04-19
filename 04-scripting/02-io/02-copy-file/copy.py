import sys
import shutil

source = sys.argv[1]
destination = sys.argv[2]
with open('D:\\School\\Semester 2\\Script talen\\04-scripting\\02-io\\02-copy-file\\a','r') as copyfile:
    with open('D:\\School\\Semester 2\\Script talen\\04-scripting\\02-io\\02-copy-file\\b','w') as destinationfile:
        shutil.copy2(copyfile,destinationfile)
        #destinationfile.write(copyfile.read())

