import sys

#with open(" ".join(sys.argv[2:3]),'r') as copyfile
#with open(" ".join(sys.arv[4:5]),'r') as destination
#copy2(data,destination)
#print(b.txt)

with open(sys.argv[2:3], 'r') as input:
    with open(sys.argv[4:5], 'w') as output:
        output.write(input.read())
