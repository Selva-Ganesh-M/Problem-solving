# merge sort
def mergeSort(arr: [int]):
  lenarr = len(arr)
  # if list has one or no elements return
  if (lenarr<2):
    return;

  # split the array
  mid = lenarr//2;
  left = arr[:mid]
  right = arr[mid:]

  # recursion
  mergeSort(left)
  mergeSort(right)

  # sorting
  i=j=k=0;
  while (i<len(left) and j<len(right)):
    if left[i]<right[j]:
      arr[k]=left[i]
      i+=1
    else:
      arr[k]=right[j]
      j+=1
    k+=1

  # adding remainig items if any
  while(i<len(left)):
    arr[k]=left[i]
    i+=1
    k+=1
    
  while(j<len(right)):
    arr[k]=right[j]
    j+=1
    k+=1
    

# arr=[5,4,7,1,6]
arr=[2,10,11,5,13,27]
print(arr)
mergeSort(arr)
print(arr)
