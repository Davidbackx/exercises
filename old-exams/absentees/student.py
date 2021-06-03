with open('all.txt','r') as all:
    with open('attending.txt','r') as attending:
        attendinglist = '\n'.join(attending.readlines())
        #print(attendinglist.lower())
        with open('absentees.txt','w') as absentees:
            for line in all.readlines():
                if line not in attendinglist:
                    print(line,file=absentees)
