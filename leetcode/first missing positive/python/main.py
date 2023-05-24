import ast
class Solution:
  def RemoveDuplicates(self, arr: [int]):
    i=0
    while (i<len(arr)-2):
      while(i+1<len(arr) and arr[i]==arr[i+1]):
        arr.pop(i+1)
      i+=1

  
  def MergeSort(self, arr):
    if(len(arr)<2):
      return;
  
    mid = (len(arr))//2
    left = arr[:mid]
    right=arr[mid:]
  
    self.MergeSort(left)
    self.MergeSort(right)
  
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


  def firstMissingPositive(self, arr: [int]):
    if len(arr) == 0: return 1
    self.MergeSort(arr)
    self.RemoveDuplicates(arr)

    # to traverse till the end of the Loop until 2nd last.
    i=0
    First = True
    while (i<len(arr)-1):
      if arr[i]>=0:
        if First and arr[i]>0:
          if arr[i]!=1:
            return 1
          else:
            First = False
        if (arr[i+1]!=arr[i]+1):
          return arr[i]+1
      i+=1
    
    if arr[i]>0:
      return 1 if First and arr[i]!=1 else arr[i]+1
    else: return 1


solution = Solution()
print(solution.firstMissingPositive(ast.literal_eval(input())))
