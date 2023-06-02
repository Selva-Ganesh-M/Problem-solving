class Stack:
  def __init__(self):
    self.__arr = []
  
  def push(self, data):
    self.__arr.append(data)
    
  def pop(self):
    return self.__arr.pop();
  
  def fill(self, arr):
    for x in arr:
      self.push(x)
      
  def isEmpty(self):
    return 1 if len(self.__arr)==0 else 0
  
  def drain(self):
    s = ""
    while not self.isEmpty():
      s+=self.pop()
    return s
stack = Stack()
stack.fill(input())
print(stack.drain())
