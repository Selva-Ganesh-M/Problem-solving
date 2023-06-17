class Stack:
  def __init__(self):
    self.stack = [];

  def push(self, data):
    self.stack.append(data);

  def pop(self):
    return self.stack.pop();

  @staticmethod
  def peek(stack):
    return stack.stack[-1] if stack.stack else None;

  def sort(self, stack):
    arr = [int(x) for x in input().split()];
    for x in arr: self.push(x);
    other = Stack();
    while (stack.stack):
      val = stack.pop()
      if not other.stack:
        other.push(val)
      else:
        if Stack.peek(other) > val:
          other.push(val);
        else:
          while (other.stack and Stack.peek(other) < val): stack.push(other.pop());
          other.push(val);
    while other.stack: print(other.pop())
      

stack = Stack();
stack.sort(stack)
