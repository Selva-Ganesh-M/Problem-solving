def RemoveDuplicates(arr: [int]):
  i=0
  while (i<len(arr)-2):
    while(len(arr[i:])>=2 and arr[i]==arr[i+1]):
      arr.pop(i+1)
    i+=1

def QuickSort(arr, start, end):

  # if array has single to no items
  if not (start<end):
    return

  pivot = start
  i=start
  j=end

  while (i<j):
    while (arr[i]<=arr[pivot]):
      i+=1
      if i>=j:
        break
    while (arr[j]>arr[pivot]):
      j-=1
    if (i<j):
      arr[i], arr[j] = arr[j], arr[i]
      i+=1
      j-=1
  else:
    arr[j], arr[pivot] = arr[pivot], arr[j]
    pivot = j

  QuickSort(arr, start, pivot-1)
  QuickSort(arr, pivot+1, end)

      



def findMissingPositiveNumber(arr):
  if(arr==[]):
    return 1
  QuickSort(arr, 0, len(arr)-1)
  RemoveDuplicates(arr)
  i=0
  First = True
  while(i<len(arr)-1):
    if (arr[i]>0):
      if First:
        if arr[i]!=1:
          return 1
        else:
          First = False
      if (arr[i+1]!=arr[i]+1):
        return arr[i]+1
    i+=1
  else:
    if arr[i]>0:
      if First and arr[i]!=1:
        return 1
      return arr[i]+1
    else:
      return 1

n=input()
print(findMissingPositiveNumber([int(x) for x in input().split()]))
