def finder(arr):

  if len(arr)==0: return 1
  template = [0 for i in range(len(arr))]
  
  for x in arr:
    if len(arr)+1>x>0:
      template[x-1]=1
  
  for i in range(len(template)):
    if template[i]==0:
      return i+1

  return len(arr)+1

input()
print(finder([int(x) for x in input().split()]))

# sample input

# 8
# -1 2 2 3 4 5
