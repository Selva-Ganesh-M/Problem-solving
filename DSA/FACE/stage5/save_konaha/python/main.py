class BHeap:
  def __init__(self):
    self.heap = [];
    
  def __fill(self, arr):
    self.heap = arr;
    
  def __maxHeapify(self, i):
    n = len(self.heap);
    lc = 2*i +1;
    rc = 2*i +2;
    if lc<n and self.heap[lc] > self.heap[i]:
      maximum = lc;
    else: maximum = i;
    if rc < n and self.heap[rc] > self.heap[maximum]:
      maximum = rc;
    if i!=maximum:
      self.heap[i], self.heap[maximum] = self.heap[maximum], self.heap[i];
      self.__maxHeapify(maximum);
    pass
  
  def __heapify(self):
    n = len(self.heap)
    last_inner_node = n//2-1;
    for i in range(last_inner_node, -1, -1):
      self.__maxHeapify(i);
  
  def __pollRemove(self):
    if not self.heap: return;
    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0];
    self.heap = self.heap[:len(self.heap)-1];
    self.__maxHeapify(0);
  
  def __poll(self):
    if not self.heap: return;
    val = self.heap[0];
    self.heap[0]//=2;
    if self.heap[0]==0:
      self.__pollRemove();
    self.__maxHeapify(0);
    return val;
  
  def saveVillage(self):
    n, z = list(map(int, input().split()));
    arr = list(map(int, input().split()));
    self.__fill(arr);
    self.__heapify();
    count = 0
    while z > 0 and self.heap:
      z-=self.__poll()
      count+=1
    print( count if self.heap or z < 0 else "Evacuate" )
  
bheap = BHeap();
bheap.saveVillage();
