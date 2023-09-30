[D, R] = [int(x) for x in input().split(" ")]

def cave(d, r):
    if (d<D-1 and r<R-1):
        return cave(d, r+1) + cave(d+1, r)
    elif (d<D-1):
        return cave(d+1, r)
    elif (r<R-1):
        return cave(d, r+1)
    else:
        return 1

print(cave(0, 0))
