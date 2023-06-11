class Node:
  def __init__(self, data):
    self.data = data;
    self.left = None;
    self.right = None;

class BT:
  def __init__(self):
    self.root = None;

  def BFS(self, queue=None):
    ans = []
    if not queue:
      if not self.root: return ans;
      queue = [self.root];
      ans.append(self.root.data)

    def __i_BFS(queue):
      while (queue):
        currLQ = queue;
        queue = [];
        for node in currLQ:
          if node.left: 
            ans.append(node.left.data);
            queue.append(node.left);
          if node.right: 
            ans.append(node.right.data);
            queue.append(node.right);

    __i_BFS(queue);
    return ans;
  
  def fill(self, arr, queue = None):
    if not queue:
      if not self.root: 
        self.root = Node(arr[0])
        arr = arr[1:]
      self.fill(arr, [self.root])
      return;
    currQ = queue;
    queue = []
    for node in currQ:
      if not arr: return;
      if arr[0]=="N":
        arr = arr[1:];
        continue;
      node.left = Node(arr[0])
      arr = arr[1:]
      queue.append(node.left);
      if not arr: return;
      if arr[0]=="N":
        arr = arr[1:];
        continue;
      node.right = Node(arr[0])
      arr = arr[1:]
      queue.append(node.right);
    if queue and arr: self.fill(arr, queue)

  def traverse(self, queue=None):
    ansArr = [];
    if not self.root: return;
    if not queue: 
      queue = [self.root]
      ansArr.append(self.root.data)
    
    def __i_traverse(queue):
      currQ = queue;
      queue = []
      for node in currQ:
        if node.left: 
          ansArr.append(node.left.data);
          queue.append(node.left)
        if node.right: 
          ansArr.append(node.right.data)
          queue.append(node.right)
      if queue: __i_traverse(queue)

    __i_traverse(queue)
    return ansArr;

  @staticmethod
  def isBST(node):
    currStatus = leftStatus = rightStatus = True;
    if node.left:
      currStatus &= node.data > node.left.data
      leftStatus = BT.isBST(node.left)
    if node.right:
      currStatus &= node.data <= node.right.data
      rightStatus = BT.isBST(node.right)
    return currStatus & leftStatus & rightStatus;

  @staticmethod
  def countNodes(node):
    if not node: return 0;
    return 1 + BT.countNodes(node.left) + BT.countNodes(node.right)
  
  @staticmethod
  def maxBST(node):
    if not node: return;
    ans=[]
    queue = [node];
    while(queue):
      currQ = queue;
      queue = [];
      for node in currQ :
        if not node: continue;
        if BT.isBST(node):
          ans.append(BT.countNodes(node))
        queue.append(node.left)
        queue.append(node.right)
    return max(ans)
        
    

bt = BT()
# bt.fill([10, 5, 15, 3,7,12,25,1,4,6,8])
bt.fill([10, 5, 15, 3,"N",12,25,1,4,6,8])
# n=input()
# bt.fill([int(x) for x in input().split()])
# print(*bt.traverse())
# print(*bt.BFS())
# print(BT.isBST(bt.root))
print(BT.maxBST(bt.root))
