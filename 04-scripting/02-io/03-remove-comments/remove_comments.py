import sys

with open(sys.argv[1],'r') as readfile:
    lines = readfile.readlines()
with open(sys.argv[1],'w') as writefile:
    for line in lines:
        if not line.find('#'):
            writefile.write(line)
            
            