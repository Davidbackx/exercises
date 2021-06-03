with open ('output.txt','w') as output:
    for i in range(0,1000000+1):
        print(i,file=output)