class Node:
  def __init__(self, data):
    self.data = data;
    self.children = [];
    
class BT:
  def __init__(self):
    self.root = None;
    
  def fill(self, arr, node=None):
    if not node:
      if not self.root:
        self.root = Node(arr[0]);
        arr = arr[1:];
        self.fill(arr, self.root);
      return;
    queue = [node];
    while queue and arr:
      current_level_queue = queue
      queue = []
      for node in current_level_queue:
        if not arr: return;
        itr = arr[0];
        if itr==0:
          arr = arr[2:];
          continue;
        else:
          arr = arr[1:]
        for i in range(itr):
          node.children.append(Node(arr[i]));
        queue.extend(node.children)
        arr = arr[itr:]
  
  def traverse(self, queue=None):
    arr = []
    def __i_traverse(arr, queue):
      if not queue:
        if not self.root: return;
        return __i_traverse(arr, [self.root]);
      currQ = queue;
      queue = [];
      for node in currQ:
        arr.append(node.data);
        queue.extend(node.children);
      if queue: __i_traverse(arr, queue);
    __i_traverse(arr, queue);
    return arr;
      
  def depthTraverse(self, queue=None):
    arr = []
    def __i_depthTraverse(arr, queue, depth=0):
      if not queue:
        if not self.root: return;
        __i_depthTraverse(arr, [self.root], depth)
        return;
      currQ = queue
      queue = [];
      for node in currQ:
        arr.append(depth);
        queue.extend(node.children);
      if queue: __i_depthTraverse(arr, queue, depth+1)
    
    __i_depthTraverse(arr, queue);
    return arr
    
bt = BT();
n=input()
bt.fill([int(x) for x in input().split()])
# arr = bt.traverse()
# print(*arr)
depthArr = bt.depthTraverse()
print(*depthArr)
    
        
    
