class Node:
  def __init__(self, data):
    self.data = data;
    self.right = None;
    self.left = None;

class BT:
  def __init__(self):
    self.root = None;

  def insert(self, value, node=None):
    if not node:
      if not self.root:
        self.root = Node(value);
        return;
      node = self.root;
    queue = [self.root];
    while queue:
      current_level_queue = queue.copy();
      queue = [];
      for node in current_level_queue:
        if not node.left: 
          node.left = Node(value)
          return;
        queue.append(node.left);
        if not node.right:
          node.right = Node(value);
          return;
        queue.append(node.right);

  def fill(self, arr):
    if not self.root:
      if arr[0]=="N": return;
      self.root = Node(arr[0]);
      arr = arr[1:]
    queue = [self.root]

    def i_fill(arr, queue):
      if not queue or not arr: return;
      nextQueue = []
      for node in queue:
        if not arr: return;
        if not node.left:
          if not arr[0]=="N":
            node.left = Node(arr[0])
            nextQueue.append(node.left);
          arr = arr[1:]
        if not arr: return;
        if not node.right:
          if not arr[0]=="N":
            node.right = Node(arr[0])
            nextQueue.append(node.right);
          arr = arr[1:]
      if arr: i_fill(arr, nextQueue);
        

    i_fill(arr, queue);
  
  def traverse(self, node=None):
    if not node:
      if not self.root: return;
      node = self.root;
      print(node.data)
    queue = [node]
    while queue:
      current_level_queue = queue.copy();
      queue = [];
      for node in current_level_queue:
        if node.left: 
          print(node.left.data)
          queue.append(node.left)
        if node.right: 
          print(node.right.data)
          queue.append(node.right)
    
  def getRightView(self, depth=0, node=None):
    arr = [];
    def i_rightViewGen(depth, node):
      if not node:
        if not self.root: return [];
        node = self.root;
      if len(arr)==depth: arr.append(node.data);
      if node.right: i_rightViewGen(depth+1, node.right);
      if node.left: i_rightViewGen(depth+1, node.left)
    i_rightViewGen(depth, node)
    return arr

bt = BT();
# for x in[1,2,3,4,5,6,7,8,9]: bt.insert(x);
bt.fill([1,2,3,4,5,6,7,8,9]);
# arr = []
# for x in input().split():
#   try:
#     arr.append(int(x))
#   except ValueError:
#     arr.append(x)
# bt.fill(arr);
# for x in [int(x) for x in input().split()]: bt.insert(x);
# bt.traverse();
rightView = bt.getRightView()
print(*rightView)
