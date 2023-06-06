class Node:
  def __init__(self, data):
    self.data = data;
    self.left = None;
    self.right = None;

class BT:
  def __init__(self):
    self.data = None;
    self.left = None;
    self.right = None;
    
  def fill(self, arr):
    if not arr: return;
    if not self.data: 
      self.data=arr[0]
      arr=arr[1:]
    queue = [self];
    while (queue and arr):
      currentNode = queue[0];
      queue = queue[1:]
      if arr:
        if arr[0]!="N":
          currentNode.left = Node(arr[0])
          queue.append(currentNode.left)
        arr=arr[1:]
      else: return;
      if arr:
        if arr[0]!="N":
          currentNode.right = Node(arr[0])
          queue.append(currentNode.right)
        arr=arr[1:]
      else: return;

  def dfs(self, node=None):
    if not node:
      if self.data:
        self.dfs(self);
      return;
    print(node.data);
    if node.left: self.dfs(node.left)
    if node.right: self.dfs(node.right)

  def zigZag(self):
    if not self.data:
      return;
    queue=[self];
    zigzag_level_order_array = [self.data]
    rev = True
    while (queue):
      currentQ = queue.copy();
      queue=[]
      current_level_items = []
      for node in currentQ:
        if node.left: 
          queue.append(node.left);
          current_level_items.append(node.left.data);
        if node.right: 
          queue.append(node.right)
          current_level_items.append(node.right.data);
      if rev:
        zigzag_level_order_array.extend(current_level_items[::-1])
      else:
        zigzag_level_order_array.extend(current_level_items)
      rev= not(rev)
    print(*zigzag_level_order_array)
        

bt = BT()
inp = [1,2,3,4,5,6,7,8,9]
# inp=[]
# for x in input().split():
#   try:
#     inp.append(int(x))
#   except:
#     inp.append(x)
bt.fill(inp)
bt.dfs()
bt.zigZag()
