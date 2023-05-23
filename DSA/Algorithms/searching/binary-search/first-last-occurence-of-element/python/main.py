def BinarySearch(arr, item, start, end):
  if(len(arr[start:end+1])==1):
    if arr[start]!=item:
      return -1
  mid =  (start+end) // 2
  if item==arr[mid]:
    return mid
  elif (item>arr[mid]):
    return BinarySearch(arr, item, mid+1, end)
  else:
    return BinarySearch(arr, item, start, mid-1)

n,src=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
found = BinarySearch(arr, src, 0, len(arr)-1)
first=found
while(True):
  if (first-1>=0):
    if arr[first-1]==src:
      first-=1
    else:
      break
  else:
    break
last=found
while(True):
  if (last+1<len(arr)):
    if arr[last+1]==src:
      last+=1
    else:
      break
  else:
    break
print(first, last)
