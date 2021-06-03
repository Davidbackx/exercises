with open('input.txt', 'r') as input:
    with open("output.txt", 'w') as output:
        for line in input:
            name = line.strip().split(':')[0]
            earnedcashed = line.strip().split(':')[1]
            startpoint = earnedcashed.strip().split(' ')[0]
            cashed = startpoint.strip().split('/')[0] 
            earned = startpoint.strip().split('/')[1] 
            extras = earnedcashed.strip().split(' ')[1]
            count1 = 0
            count2 = 0
            for extra in extras:
                if extra == '+':
                    count1 += 1
                elif extra == '-':
                    count2 += 1

            earned2 = int(earned) + count1
            cashed2 = int(cashed) + count2
        
            print(f'{name}:{cashed2}/{earned2}', file = output)