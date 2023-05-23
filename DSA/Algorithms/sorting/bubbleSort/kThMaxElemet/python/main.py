def kthMaxElementFind(arr: [int], k):
  count = 0
  end = len(arr)-1
  while (count!=k):
    i=0
    while (i<end):
      if (arr[i]>arr[i+1]):
        arr[i], arr[i+1] = arr[i+1], arr[i]
      i+=1;
    end-=1;
    count+=1
  return (arr[len(arr)-k])

n = input()
arr = [int(x) for x in input().split()]
k = int(input())
print(kthMaxElementFind(arr, k))
