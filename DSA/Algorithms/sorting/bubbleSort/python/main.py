# Bubble sort
def BS(arr:[int]):
  for i in range(len(arr)-1):
    print(arr)
    for j in range(len(arr)-1):
      if(arr[j]>arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

print(BS([6,5,4,3,2,1]))
