class Node:
  def __init__(self, data):
    self.data = data;
    self.left = None;
    self.right = None;
    
class BST:
  def __init__(self):
    self.root = None;
    self.stack = None;
    self.stackTouched = False;
    
  def __push(self, node):
    if not self.stack:
      self.stack = [node]
    else:
      self.stack.append(node)
  
  def __pop(self):
    if not self.stack: return None;
    return self.stack.pop();
  
  def __peek(self):
    if not self.stack: return None;
    return self.stack[-1];
  
  def fill(self, value, node=None):
    if not node:
      if not self.root: 
        self.root = Node(value);
        return;
      node = self.root;
    if value < node.data:
      if not node.left:
        node.left = Node(value);
      else:
        self.fill(value, node.left);
    else:
      if not node.right:
        node.right = Node(value);
      else:
        self.fill(value, node.right);
        
  def inOrder(self, node=None):
    ans = []
    if not node:
      if not self.root: return ans;
      node = self.root;
    def __i_inOrder(node):
      if node.left: __i_inOrder(node.left);
      ans.append(node.data);
      if node.right: __i_inOrder(node.right);
    __i_inOrder(node);
    return ans;
  
  def __createStack(self):
    if self.stackTouched: return;
    if not self.root: return;
    node = self.root;
    while(node):
      self.__push(node);
      node = node.left;
    self.stackTouched = True
    
  
  def __pullRightZag(self, node):
    if node.right:
      node = node.right;
      while (node):
        self.__push(node);
        node = node.left;
  
  def __hasNext(self):
    if not self.stack:
      self.__createStack();
    return True if self.__peek() else False;
  
  def __next(self):
    if not self.stack:
      self.__createStack();
    nextItem = self.__pop();
    self.__pullRightZag(nextItem);
    return nextItem.data;
    
  def handleCommands(self, commands):
    ans = [];
    for command in commands:
      if command == "next":
        ans.append(self.__next());
      elif command == "hasNext":
        ans.append(self.__hasNext());
    return ans;
    
n = input()
data = [int(x) for x in input().split()]
commands = [x for x in input().split()]
bst = BST();
for x in data: bst.fill(x);
ans = bst.handleCommands(commands)
print(*ans)
# inOrder = bst.inOrder();
# print(*inOrder)


# 5
# 7 3 15 9 20
# next next hasNext next next next hasNext