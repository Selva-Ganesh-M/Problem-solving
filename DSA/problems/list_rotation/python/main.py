def rotateArray(arr, times, start, end, rotation="f"):
  if rotation == "f":
    for i in range(times):
      temp = arr[end];
      for j in range(end, start, -1):
        arr[j]=arr[j-1]
      arr[start]=temp
  else:
    for i in range(times):
      temp = arr[start];
      for j in range(start, end):
        arr[j]=arr[j+1]
      arr[end]=temp


# to rotate whole array
# rotateArray(arr, 3, 0, len(arr)-1)

# to rotate a particular section of it backwards
# rotateArray(arr, 2, 0, 2, "b")

n=input()
arr=list(map(int, input().split()))
t=int(input())
[s,e]=list(map(int, input().split()))
rotateArray(arr, t, s, e, "b")

print(arr)      
