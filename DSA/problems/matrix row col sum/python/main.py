r=int(input())
c=int(input())
mat = [[int(x) for x in input().split()] for i in range(r)]
rsums = []
csums = []
if r==c:
  for i in range(r):
    rs=cs=0
    for j in range(c):
      rs+=mat[i][j]
      cs+=mat[j][i]
      
    rsums.append(rs)
    csums.append(cs)
else:
  for i in range(r):
    s=0
    for j in range(c):
      s+=mat[i][j]
    rsums.append(s)
  for i in range(c):
    s=0
    for j in range(r):
      s+=mat[j][i]
    csums.append(s)
  
l1="The Sum of rows is"
for x in rsums:
  l1+=" "
  l1+=str(x)
l2="The Sum of columns is"
for x in csums:
  l2+=" "
  l2+=str(x)

print(l1)
print("Row {} has a maximum sum".format(rsums.index(max(rsums))+1))
print(l2)
print("Column {} has the maximum sum".format(csums.index(max(csums))+1))

#3
#2
#1 0
#-8 13
#34 65

