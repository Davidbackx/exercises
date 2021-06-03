import re
with open('input.txt','r')as input:
    with open('output.txt','w') as output:
        ids = list()
        for line in input.readlines():
            i_d=re.findall(r'(R[0-9]{7}|s[0-9]{7}|U[0-9]{7})',line,re.IGNORECASE)
            ids.append('\n'.join(i_d))
        for id in ids:
            if id.startswith('u'):
                print(f'{id.lower()}@ucll.be',file=output)
            else:
                print(f'{id.lower()}@student.ucll.be',file=output)