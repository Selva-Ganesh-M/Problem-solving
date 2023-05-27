def spiral(arr, t,b,l,r, stop):
  expCount=(b+1)*(r+1);
  count=0
  stri=""
  while (count<expCount):
    # move right
    for i in range(l, r+1):
      stri+=str(arr[t][i])+" "
      count+=1
    else:
      t+=1
      if count>=expCount:
        break
  
    # move down
    for i in range(t, b+1):
      stri+=str(arr[i][r])+" "
      count+=1
    else:
      r-=1
      if count>=expCount:
        break
  
    # move left
    for i in range(r, l-1, -1):
      stri+=str(arr[b][i])+" "
      count+=1
    else:
        b-=1
        if count>=expCount:
          break
  
    # move up
    for i in range(b, t-1, -1):
      stri+=str(arr[i][l])+" "
      count+=1
    else:
      l+=1
      if count>=expCount:
        break
  
  return stri[:len(stri)-1]


[r,c]=[int(x) for x in input().split()]

arr = [[int(y) for y in input().split()] for x in range(r)]

rp=len(arr)-1
cp=len(arr[0])-1
stop=False
def spiral(arr, t,b,l,r, stop):
  expCount=(b+1)*(r+1);
  count=0
  stri=""
  while (count<expCount):
    # move right
    for i in range(l, r+1):
      stri+=str(arr[t][i])+" "
      count+=1
    else:
      t+=1
      if count>=expCount:
        break
  
    # move down
    for i in range(t, b+1):
      stri+=str(arr[i][r])+" "
      count+=1
    else:
      r-=1
      if count>=expCount:
        break
  
    # move left
    for i in range(r, l-1, -1):
      stri+=str(arr[b][i])+" "
      count+=1
    else:
        b-=1
        if count>=expCount:
          break
  
    # move up
    for i in range(b, t-1, -1):
      stri+=str(arr[i][l])+" "
      count+=1
    else:
      l+=1
      if count>=expCount:
        break
  
  return stri[:len(stri)-1]


[r,c]=[int(x) for x in input().split()]

arr = [[int(y) for y in input().split()] for x in range(r)]

rp=len(arr)-1
cp=len(arr[0])-1
stop=False
print(spiral(arr, 0,rp,0,cp, stop))def spiral(arr, t,b,l,r, stop):
  expCount=(b+1)*(r+1);
  count=0
  stri=""
  while (count<expCount):
    # move right
    for i in range(l, r+1):
      stri+=str(arr[t][i])+" "
      count+=1
    else:
      t+=1
      if count>=expCount:
        break
  
    # move down
    for i in range(t, b+1):
      stri+=str(arr[i][r])+" "
      count+=1
    else:
      r-=1
      if count>=expCount:
        break
  
    # move left
    for i in range(r, l-1, -1):
      stri+=str(arr[b][i])+" "
      count+=1
    else:
        b-=1
        if count>=expCount:
          break
  
    # move up
    for i in range(b, t-1, -1):
      stri+=str(arr[i][l])+" "
      count+=1
    else:
      l+=1
      if count>=expCount:
        break
  
  return stri[:len(stri)-1]


[r,c]=[int(x) for x in input().split()]

arr = [[int(y) for y in input().split()] for x in range(r)]

rp=len(arr)-1
cp=len(arr[0])-1
stop=False
print(spiral(arr, 0,rp,0,cp, stop))





# arr=[
#   [1, 2, 3, 4, 5, 6],
#   [7, 8, 9, 10,11,12],
#   [13,14,15,16,17,18]
# ]
# arr=[
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# arr=[
#   [1,2,3,10],
#   [4,5,6,11],
#   [7,8,9,13]
# ]