class Node:
  def __init__(self, data):
    self.data = data;
    self.next = None;

class LinkedList:
  def __init__(self):
    self.head = None;
    
  def fill(self, arr):
    for x in arr:
      self.append(x);

  def append(self, data):
    newNode = Node(data);
    if not self.head:
      self.head = newNode;
    else:
      current = self.head;
      while current.next:
        current = current.next;
      current.next = newNode;
  
  def __add__(self, other):
    string=""
    s=''
    sc = self.head;
    oc = other.head;
    while (sc and oc):
      s=str(sc.data + oc.data + (int(s) if s else 0))
      string+=s[-1]
      s=s[:len(s)-1]
      sc = sc.next;
      oc = oc.next;
    while (sc):
      s=str(sc.data+(int(s) if s else 0))
      string+=s[-1]
      s=s[:len(s)-1]
      sc = sc.next;
    while (oc):
      s=str(oc.data+(int(s) if s else 0))
      string+=s[-1]
      s=s[:len(s)-1]
      oc = oc.next;
    return string+s;

stack1 = LinkedList()
print("enter space seperated first linked list items:")
stack1.fill([int(x) for x in input().split()])
stack2 = LinkedList()
print("enter space seperated second linked list items:")
stack2.fill([int(x) for x in input().split()])
print(*list(stack1+stack2))
