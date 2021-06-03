

with open('input.txt','r') as input:
    git = []
    gitlog = []
    with open('output.txt','w') as output:
        for line in input.readlines():
            git.append(line)
            gitlog.append(git.split(1000))