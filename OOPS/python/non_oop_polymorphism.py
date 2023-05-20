
def s(x, y=0, z=0):
  return x+y+z

print(s(*[int(x) for x in input().split()]))
