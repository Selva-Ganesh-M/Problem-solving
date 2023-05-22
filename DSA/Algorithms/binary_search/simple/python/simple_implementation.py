
def LinearSort(lis):
  for i in range(len(lis)):
    for j in range(i+1, len(lis)):
      if lis[i]>lis[j]:
        lis[i], lis[j] = lis[j], lis[i]
  return lis

def BinarySearch(sorted_list, src, sp, lp):
  if sp>lp: return "Not Found"
    
  # mid finding
  mid = (sp+lp)//2
  midItem = sorted_list[mid]
  print(sorted_list[sp:lp+1], midItem)
  
  # if mid is search return item
  if midItem==src: return midItem

  # if src is lesser than mid
  if midItem>src:
    lp = mid-1
    
  # if src is greater than mid
  if midItem<src:
    sp = mid+1

  return BinarySearch(sorted_list, src, sp, lp)



inp = [1, 4, 5, 9 ,10, 11, 35, 99]
# inp = [int(x) for x in input().split()]
src = 99
# src = int(input())
sorted_list = LinearSort(inp)
sp=0
lp=len(sorted_list)-1
print(BinarySearch(sorted_list, src, sp, lp))
