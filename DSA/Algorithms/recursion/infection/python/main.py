def isValidPos(i, j):
  return 0<=i<M and 0<=j<N
  
def isCv(i ,j):
  return isValidPos(i, j) and arr[i][j] in ["c", "v"]

def canSpread(i, j):
  return isValidPos(i, j) and not isCv(i, j)

def spread(arr, ground):
  if ground==[]: return 0
  count=0
  temp = []
  for [i, j] in ground:
    if (not (isValidPos)) or isCv(i, j):
      continue
    count=1
    arr[i][j]="v"
    if canSpread(i, j-1): temp.append([i, j-1])
    if canSpread(i, j+1): temp.append([i, j+1])
    if canSpread(i-1, j): temp.append([i-1, j])
    if canSpread(i+1, j): temp.append([i+1, j])
  ground = temp
  return count + spread(arr, ground)

print("enter the M and N value for M X N matrix: ")
print("eg. 10 10")
print()
[M, N] = [int(x) for x in input().split()]
print("enter the values 'o' for open and 'c' closed.")
print('''eg.
o o o o o c c c c c
c o o c o c o c o c
o o o o o o o o o o
c c c c c c c c c c
o c o c o c o c o c
c o o o o o o o o c
o o o o o o o o o o
c c c c c c c c c c
o o o o o c c c c c
o o c c c c c c c c
''')
print()
arr = [[x for x in input().split()] for i in range(M)]
print("enter the i and j value for i X j room from which the infection has been started to spread: ")
print("eg. 2 2")
print()
[i, j] = [int(x) for x in input().split()]
print("No of minutes:", spread(arr, [[i,j]]))

