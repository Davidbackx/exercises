import re

timeslist = list()
with open ('input.txt','r') as input:  
    with open('output.txt','w') as output:
        line_index = 0
        lines = input.readlines()
        timeslist.extend(re.findall(r'([0-9]{2}:[0-9]{2}:[0-9]{2})',str(lines)))
        for time in timeslist:
            line_index += 1
            hours = time[:2]
            minutes = time[3:5]
            seconds = time[6:8]
            if int(hours) > 23 or int(minutes) > 59 or int(seconds) > 59:
                print(f'{line_index} {time}',file=output)
            
