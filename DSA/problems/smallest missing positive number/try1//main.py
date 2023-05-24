def RemoveDuplicates(arr: [int]):
  i=0
  while (i<len(arr)-2):
    while(len(arr[i:])>=2 and arr[i]==arr[i+1]):
      arr.pop(i+1)
    i+=1

def MergeSort(arr):
  if(len(arr)<2):
    return;

  mid = (len(arr))//2
  left = arr[:mid]
  right=arr[mid:]

  MergeSort(left)
  MergeSort(right)

  i=j=k=0
  while (i<len(left) and j<len(right)):
    if (left[i]<right[j]):
      arr[k]=left[i]
      k+=1
      i+=1
    else:
      arr[k]=right[j]
      k+=1
      j+=1

  # adding remaining items
  while (i<len(left)):
    arr[k]=left[i]
    i+=1
    k+=1
    
  while j<len(right):
    arr[k]=right[j]
    j+=1
    k+=1
 

def findMissingPositiveNumber(arr):
  if(arr==[]):
    return 1
  MergeSort(arr)
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



# first line number of items.
# space seperated list items.
