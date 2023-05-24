def mergeSort(arr):
  pass

def binarySearch(arr, src, start, end):
  if arr[start:end]==[]:
    return -1 
  mid = (start+end)//2
  if arr[mid]==src:
    return mid
  if (src<arr[mid]):
    return binarySearch(arr, src, start, mid-1)
  if (src>arr[mid]):
    return binarySearch(arr, src, mid+1, end)

arr=[-1,0,7,99,676]
print(binarySearch(arr, 9, 0, len(arr)-1))
