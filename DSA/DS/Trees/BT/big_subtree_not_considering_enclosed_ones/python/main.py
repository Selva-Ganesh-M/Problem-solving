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

  def BST_size(self, node=None):
    if not node:
      if not self.data: 
        return 0;
      else: return self.BST_size(self)
    isBST = True;
    lCount=rCount=0
    if node.left:
      lCount = self.BST_size(node.left);
      if node.left.data > node.data:
        isBST = False;
    if node.right:
      rCount = self.BST_size(node.right);
      if node.right.data < node.data:
        isBST = False;
    return lCount + rCount + 1 if isBST else max([lCount, rCount]) 

bt = BT()
inp = [15, 10, 20, 8, 12, 16, 25]
# inp = [5,2,4,1,3]
# inp = []
# inp = [60, 65, 70, 50]
# inp=[]
# for x in input().split():
#   try:
#     inp.append(int(x))
#   except:
#     inp.append(x)
bt.fill(inp)
# bt.dfs()
print(bt.BST_size())
