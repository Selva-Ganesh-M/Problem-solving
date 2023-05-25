def binarySearch(arr, src):
  start = 0;
  end = len(arr)-1;

  while (start<end):
    mid = (start+end)//2;
    if arr[mid]==src:
      return mid
    elif (src<arr[mid]):
      end = mid-1
    else:
      start = mid+1
  else:
    return start if (start==end and arr[start]==src) else -1


arr=[1,2,3,4,5]
# arr=[]
# arr=[-1,-2,-3,0]
# arr=[4,5,6,7,8]
# hhh

print(binarySearch(arr, 7))
