def pascalsTriangle(num):
  arr = [
    [1],
    [1,1],
  ]

  while (len(arr)!=num):
    temp = [];
    lastStep = arr[-1];
    temp.append(lastStep[0]);
    for i in range(len(lastStep)-1):
      temp.append(lastStep[i]+lastStep[i+1]);
    temp.append(lastStep[-1]);
    arr.append(temp)

  for x in arr:
    print(*x)

pascalsTriangle(int(input("enter the height of the triangle: ")))
      
