def isMinHeap(heap):
  n = len(heap);
  last_inner = n//2 - 1;
  for i in range(last_inner, -1, -1):
    curr = i;
    lc = 2 * i + 1;
    rc = 2 * i + 2;
    if (lc < n and heap[lc] < heap[curr]) or ( rc< n and heap[rc] < heap[curr]):
      return False;
  return True;

n = input()
arr = list(map(int, input().split()));
print("Given array is a min heap" if isMinHeap(arr) else "Given array is not a min heap")
