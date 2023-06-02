class Stack:
  def __init__(self):
    self.__s = []

  def push(self, data):
    self.__s.append(data)

  def pop(self):
    return self.__s.pop()

  def top(self):
    return -1 if not self.empty() else self.__s[-1]

  def empty(self):
    return True if len(self.__s) == 0 else False

  def fill(self, arr):
    for x in arr:
      self.push(x)
    
  def drain(self):
    arr=[]
    while not self.empty():
      arr.append(self.pop())
    return arr
  
  def mySort(self, arr, i=0, j=1, clear=1):
    if len(arr)<=1: return;
    if j==len(arr):
      return self.mySort(arr) if not clear else None;
    if (arr[i]>arr[j]):
      arr[i], arr[j] = arr[j], arr[i];
      clear = 0
    return self.mySort(arr, i+1, j+1, clear)

  def printAns(self, arr):
    self.fill(arr);
    arr = self.drain();
    self.mySort(arr);
    self.fill(arr);
    arr = self.drain()
    print(*arr)

stack = Stack()
# n = int(input())
print("please enter the space seperated list values: ")
stack.printAns([int(x) for x in input().split()])
