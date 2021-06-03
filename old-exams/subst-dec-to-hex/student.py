#print(hex(20))
import re
#with open('input.txt','r') as input:
#    lines = input.readlines()
#    listvanGetallen = list()
#    for line in lines:
#       listvanGetallen.extend((re.findall(r'HEX\(([0-9]+)\)',line)))
#    print(listvanGetallen)
    
with open('input.txt','r') as input:
    with open('output.txt','w') as output:
        for line in input.readlines():
            decgetal = re.findall(r'HEX\(([0-9]+)\)',line)
            output.write(line.replace(decgetal for decgetal in decgetal ,hex(decgetal)))
            
