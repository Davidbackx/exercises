open with(sys.argv[1],'r') as file:
for s in file:
    i = line.find('#')
    remove