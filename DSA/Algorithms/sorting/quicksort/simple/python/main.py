# quicksort
def QS(arr, start, end):
  if not (start<end):
    return
  pivot = start;
  i=start
  j = end
  while(i<j):
    while not (arr[i]>arr[pivot]):
      i+=1
      if not (i<j):
        break
    while not (arr[j]<=arr[pivot]):
      j-=1
    if (i<j):
      arr[i], arr[j] = arr[j], arr[i]
      i+=1
      j-=1
  else: 
    arr[j], arr[pivot] = arr[pivot], arr[j]
    pivot = j
  QS(arr, start, pivot-1)
  QS(arr, pivot+1, end)

arr=[7, 6, 10, 5, 9, 2, 1, 15, 7]
# arr=[8, 1, 2,3, 65, 4, 34, 7, 9]
print(QS(arr, 0, len(arr)-1))
print(arr)
    


