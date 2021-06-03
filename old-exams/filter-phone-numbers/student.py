import re

with open('input.txt', 'r') as input_file:
    with open('output.txt','w') as output_file:
        numbers = list()
        for line in input_file:
            if re.fullmatch(r'(0|\+32-)4[56789]\d-\d{2}-\d{2}-\d{2}',line.strip()):
                output_file.write(line)
        
            