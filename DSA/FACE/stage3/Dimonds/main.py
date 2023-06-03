


# from collections import deque as dq

# class Queue:
#   def __init__(self):
#     self.queue = dq([])

#   def fill(self, arr):
#     for x in arr:
#       self.queue.append(x);

#   def __max(self):
#     maxPos = 0;
#     for i in range(len(self.queue)):
#       if self.queue[maxPos]<self.queue[i]:maxPos=i;
#     maxItem = self.queue[maxPos]
#     self.queue.remove(maxItem)
#     self.queue.insert(maxPos, maxItem//2)
#     return maxItem;

#   def steal(self, k):
#     sum = 0
#     for i in range(k):
#       sum+=self.__max()
#     return sum;

# [n,k] = [int(x) for x in input().split()]
# arr = [int(x) for x in input().split()]
# q = Queue()
# q.fill(arr)
# print(q.steal(k))

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Node:
  def __init__(self, data):
    self.data = data;
    self.next = None;

class Queue:
  def __init__(self):
    self.head = None;

  def enque(self, data):
    if not self.head:
      self.head = Node(data);
      return;
    current = self.head;
    while(current.next): current = current.next;
    current.next = Node(data);
    
  def fill(self, arr):
    if not self.head: 
      self.head = Node(arr[0]);
      arr=arr[1:];
    for x in arr:
      self.enque(x);

  def getMaxAndReduce(self):
    if not self.head: return 0;
    maxN = self.head;
    current = self.head;
    while (current):
      if current.data > maxN.data: maxN = current;
      current = current.next
    ans = maxN.data;
    maxN.data = maxN.data//2;
    return ans;
    
  def steal(self, k):
    sum = 0
    for i in range(k):
      sum+=self.getMaxAndReduce()
    return sum;
    

[n,k] = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
q = Queue()
q.fill(arr)
print(q.steal(k))

# '''''''''''''''''''''''''''''''''''''''''''''''''

# [n,k] = [int(x) for x in input().split()]
# arr = [int(x) for x in input().split()]
# sum=0
# for i in range(k):
#   sum+=max(arr)
#   arr[arr.index(max(arr))]//=2;
# print(sum)
    
# '''''''''''''''''''''''''''''''''''''''''''''''''



