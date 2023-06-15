
class Node:
  def __init__(self, data):
    self.data = data;
    self.left = None;
    self.right = None;


class BHeap:
  def __init__(self):
    self.heap = [];

  def __fill(self, arr):
    self.heap = arr;

  def __min_heapify(self, i):
    length = len(self.heap);
    lc = 2 * i + 1;
    rc = 2 * i + 2;
    minimum = lc if lc < length and self.heap[lc]< self.heap[i] else i
    if rc < length  and self.heap[rc] < self.heap[minimum]: minimum = rc;
    if minimum != i:
      self.heap[i], self.heap[minimum] = self.heap[minimum], self.heap[i]
      self.__min_heapify(minimum);

  def __heapify(self):
    n = len(self.heap);
    last_inner_node = n//2 - 1;
    for i in range(last_inner_node, -1, -1):
      self.__min_heapify(i);

  def __poll(self):
    self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0];
    ans = self.heap[len(self.heap)-1];
    self.heap = self.heap[:len(self.heap)-1]
    self.__min_heapify(0)
    return ans;
  
  def merKarr(self, arr):
    for x in arr: self.heap.extend(x);
    self.__heapify();
    ans = []
    while self.heap:
      ans.append(self.__poll());
    return ans;

heap = BHeap()
# k = int(input());
# n = input()
# arr = [[int(x) for x in input().split()] for i in range(k)]
arr = [
  [111, 112, 500],
  [0 ,1, 8],
  [2, 4, 7, 52]
];
ans = heap.merKarr(arr)
print(ans)



