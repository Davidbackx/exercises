from datetime import  datetime


def is_valid(string):
    try:
        datetime.strptime(string, '%d-%m-%Y')
        return True
    except ValueError:
        return False

with open('input.txt', 'r') as input:
    with open('output.txt', 'w') as output:
        for line in input:
            line = line.strip()
            if is_valid(line):
                print(line,file=output)


            