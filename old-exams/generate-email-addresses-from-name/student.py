import re

with open('input.txt','r') as input:
    with open('output.txt','w') as output:
        for name in input.readlines():
            lnames = re.findall(r'([a-zA-Z]+)',name)
            fname = lnames[:1]        
            lname = lnames[1:]
            l_name = "".join(lname).lower()
            f_name = "".join(fname).lower()
            print(f'{f_name}.{l_name}@student.ucll.be',file=output)