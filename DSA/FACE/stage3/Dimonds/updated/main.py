
class PQueue:
  def __init__(self):
    self.heap = [];

  def fill(self, arr):
    self.heap = arr;

  def peek(self):
    return None if not self.heap else self.heap[0];

  
  def __min_heapify(self, i):
    n=len(self.heap);
    lc = (i*2) + 1
    rc = (i*2) + 2
    if (lc < n and self.heap[lc] < self.heap[i]):
      smaller = lc;
    else:
      smaller = i;
    if (rc < n and self.heap[rc] < self.heap[smaller]):
      smaller = rc;
    if smaller!=i:
      self.heap[i], self.heap[smaller] = self.heap[smaller], self.heap[i]
      self.__min_heapify(smaller);
      
  def __max_heapify(self, i):
    n=len(self.heap);
    lc = (i*2) + 1
    rc = (i*2) + 2
    if (lc < n and self.heap[lc] > self.heap[i]):
      greater = lc;
    else:
      greater = i;
    if (rc < n and self.heap[rc] > self.heap[greater]):
      greater = rc;
    if greater!=i:
      self.heap[i], self.heap[greater] = self.heap[greater], self.heap[i]
      self.__max_heapify(greater);

  def steal(self):
    if not self.heap: return None;
    if len(self.heap)==1: 
      val = self.peek();
      self.heap[0] = self.heap[0]//2;
      return val;
    min = False if self.heap[0] - self.heap[-1] > 0 else True
    val = self.peek();
    self.heap[0]//=2;
    self.__min_heapify(0) if min else self.__max_heapify(0);
    return val;
        
    
  
  def heapify(self, **kwargs):
    if not self.heap: return;
    min = True;
    if kwargs and kwargs["max"]:
      min = False;
    n = len(self.heap);
    inner_node_end = (n//2) - 1;
    for i in range(inner_node_end, -1, -1):
      self.__min_heapify(i) if min else self.__max_heapify(i)

  def display(self):
    print(self.heap)

# priority queue - max heap
[n, times] = [int(x) for x in input().split()];
pQueue = PQueue()
pQueue.fill([int(x) for x in input().split()])
pQueue.heapify(max=True)
money = 0;
for i in range(times): money+=pQueue.steal()
print(money)

# # priority queue - min heap
# pQueue = PQueue()
# pQueue.fill([5,7,1,3,4,9,8,2,11])
# pQueue.heapify()
# pQueue.display()
# pQueue.poll();
# pQueue.display()
