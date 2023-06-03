

class Node:
  def __init__(self, data):
    self.data = data;
    self.next = None;

class Queue:
  def __init__(self):
    self.head = None

  def fill(self, arr):
    last = self.head;
    if last:
      while (last.next):
        last = last.next;
    else:
      new = Node(arr[0])
      self.head = new;
      arr=arr[1:]
    for x in arr:
      new = Node(x)
      if not last: last = self.head
      last.next = new;
      last = last.next;

  def enque(self, data):
    new = Node(data);
    if not self.head:
      self.head = new;
    else:
      current = self.head;
      while(current.next):
        current = current.next
      current.next = new

  def deque(self):
    if not self.head: return;
    if not self.head.next:
      self.head = None;
      return;
    current = self.head;
    self.head = self.head.next;
    current.next = None

  def traverse(self):
    if not self.head: return;
    current = self.head;
    arr=[]
    while (current):
      arr.append(current.data)
      current = current.next
    print(*arr)

queue = Queue()
queue.fill([1,2,3,4,5])
queue.traverse()
queue.enque(10)
queue.traverse()
queue.deque()
queue.traverse()
queue.deque()
queue.traverse()
queue.deque()
queue.traverse()
queue.deque()
queue.traverse()
queue.deque()
queue.traverse()
queue.deque()
queue.traverse()
queue.deque()
queue.traverse()
queue.deque()
queue.traverse()
