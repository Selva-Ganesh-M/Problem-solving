class BHeap:
  def __init__(self):
    self.heap = None;
    
  def __max_heapify(self, i=0):
    if not self.heap: return;
    n = len(self.heap);
    lc = 2*i + 1;
    rc = 2*i +2;
    if lc<n and self.heap[lc][0] > self.heap[i][0]:
      maximum = lc;
    else: maximum = i;
    if rc < n and self.heap[rc][0] > self.heap[maximum][0]:
      maximum = rc;
    if i!=maximum:
      self.heap[i], self.heap[maximum] = self.heap[maximum], self.heap[i];
      self.__max_heapify(maximum);
    
  
  def __insert(self, tup):
    if not self.heap: 
      self.heap = [tup];
    else:
      arr = [tup];
      arr.extend(self.heap)
      self.heap = arr;
      self.__max_heapify();
  
  def __poll(self):
    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0];
    out = self.heap[-1];
    self.heap = self.heap[:len(self.heap)-1]
    self.__max_heapify();
    return out;
    
  def getCandies(self):
    N, D = list(map(int, input().split()));
    prices = list(map(int, input().split()));
    sweetness = list(map(int, input().split()));
    for tup in zip(sweetness, prices): self.__insert(tup);
    candies_count = 0
    res_sweetness = 0
    while candies_count < 2 and D > 0 and self.heap:
      sweetness, price = self.__poll();
      if price <= D:
        D-=price
        candies_count+=1;
        res_sweetness += sweetness;
    print(res_sweetness);

bheap = BHeap()
bheap.getCandies();        
    
