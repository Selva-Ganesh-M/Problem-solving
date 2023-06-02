class Node:
  def __init__(self, data):
    self.prev = None;
    self.next = None;
    self.data = data;

class DLL:
  def __init__(self):
    self.head = None

  def fill(self, arr):
    if not self.head:
      self.head = Node(arr[0])
    arr=arr[1:]
    current = self.head
    for x in arr:
      new = Node(x)
      current.next = new
      new.prev = current
      current = new

  def print_list(self):
    current = self.head
    arr = []
    while(current):
      arr.append(current.data)
      current = current.next
    print(*arr)

  def rotate(self, turns):
    for i in range(turns):
      current = self.head;
      last = self.head
      while (last.next):
        last = last.next
      self.head = self.head.next
      current.next = None;
      self.head.prev = None;
      current.prev = last;
      last.next = current;
      last = current;
    self.print_list()
      

testcases = int(input("enter the number of testcases: "))
for i in range(testcases):
  dll = DLL()
  print("enter the length of array and turns of rotations: ")
  print("eg. 6 2")
  [length, turns] = [int(x) for x in input().split()]
  print("enter the space seperated array items: ")
  dll.fill([int(x) for x in input().split()])
  print("rotated dll:")
  dll.rotate(turns)
  print()
