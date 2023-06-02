
class Stack:
  def __init__(self):
    self.__s = []

  def __push(self, data):
    self.__s.append(data)

  def __pop(self):
    return self.__s.pop()

  def __peek(self):
    return self.__s[-1]

  def __stackUnderflow(self):
    return True if len(self.__s) == 0 else False
    
  def isBalanced(self, string):
    dic={
      "(":")",
      "{":"}",
      "[":"]"
    }
    for x in string:
      if self.__stackUnderflow():
        self.__push(x)
        continue;
      if self.__peek() not in dic: return False
      if x == dic[self.__peek()]:
        self.__pop()
      else:
        self.__push(x)
    return self.__stackUnderflow()

stack = Stack()
print("Balanced" if stack.isBalanced(input("Enter the bracket pairs (eg.[]{()}): ")) else "Not Balanced")
