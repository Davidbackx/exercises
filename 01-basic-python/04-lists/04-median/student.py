# Write your code here
def median(ns):
    xs = list
    xs = sorted(ns)
    length = len(xs)
    if length % 2 == 0:
        return (xs[length//2] + xs[length // 2 -1])/2       
    else:
        return xs[length//2]

