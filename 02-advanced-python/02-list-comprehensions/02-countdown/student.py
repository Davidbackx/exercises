# Write your code here
def countdown(n):
    string = ""
    for x in range(n,0,-1):
        string += str(x) +", "
    return string
