
class Node:
  def __init__(self, data):
    self.data = data;
    self.next = None;

class Queue:
  def __init__(self):
    self.head = None;
    self.ans = "";
  def addToLast(self, data):
    newNode = Node(data);
    if not self.head:
      self.head = newNode
    else:
      last = self.head
      while(last.next):
        last = last.next;
      last.next = newNode;

  def remove(self, data):
    # tracking current and previous nodes
    current = self.head;
    prev = None;

    # if first node is the expected node.
    if current.data == data:
      # if there is no other nodes
      if not current.next:
        self.head = None;
        return;
      # if there are other nodes
      else:
        self.head = current.next
        current.next = None;
        return;

    # when expected node is not the first node.
    # selecting the expected node
    while (current.next):
      prev = current;
      current = current.next;
      if current.data == data:
        break;

    # if expected node is the last node
    if not current.next:
      prev.next=None
      return;

    # if expected node is somewhere in the middle
    next = current.next
    prev.next = next;
    current.next = None;
      
    
  def evaluate(self, string):
    lis=[[0,0] for i in range(26)];
    for s in string:
      pos = ord(s)-97
      if lis[pos][0]<=0:
        self.addToLast(s)
        lis[pos][0]=1
        lis[pos][1]=1
      else:
        lis[pos][0]+=1
        if lis[pos][1]:
          self.remove(s);
          lis[pos][1]=0;
      self.ans += self.head.data if self.head else "*";
      
queue = Queue()
queue.evaluate(input())
print(queue.ans)
  
