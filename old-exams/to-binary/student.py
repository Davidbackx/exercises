from os import write


with open('input.txt') as input:
    lines = input.readlines()
    listOfNumbers = list()
    for line in lines:
        number = int(line)
        listOfNumbers.append(bin(number)[2:])
    
    with open('output.txt','w')as output:
        output.write('\n'.join(listOfNumbers))
