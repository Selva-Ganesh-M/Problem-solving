
class Node:
  def __init__(self, data):
    self.data = data;
    self.left = None;
    self.right = None;


class BT:
  def __init__(self):
    self.root = None;

  def insert(self, arr, queue=[]):
    if not arr: return;
    if not queue:
      while arr and arr[0]=="N": arr=arr[1:]
      if not arr: return;
      self.root = Node(arr[0]);
      return self.insert(arr[1:], [self.root]);
    while queue:
      tempQueue = queue.copy();
      queue=[];
      for node in tempQueue:
        if node.data == 6: print("6", *arr)
        
        # creating the left node
        if not arr: return;
        if arr[0]!="N":
          node.left = Node(arr[0]);
          queue.append(node.left);
          arr=arr[1:]
        else:
          arr=arr[1:]
        
        # creating the right node
        if not arr: return;
        if arr[0]!="N":
          node.right = Node(arr[0])
          queue.append(node.right);
          arr=arr[1:]
        else:
          arr=arr[1:]

  def traverse(self, queue=None):
    if not queue:
      if self.root: 
        print(self.root.data);
        self.traverse([self.root]);
      return;
    while (queue):
      qcp = queue.copy();
      queue =  [];
      nodes_in_current_section = []
      for node in qcp:
        if node.left:
          nodes_in_current_section.append(node.left.data);
          queue.extend([node.left]);
        if node.right:
          nodes_in_current_section.append(node.right.data);
          queue.extend([node.right]);
      print(*nodes_in_current_section)

  def depthTraverse(self, dic, depth=0, node=None):
    if not node:
      if self.root:
        self.depthTraverse(dic, depth, self.root);
      return;
    dic[depth]=node.data;
    if node.left: self.depthTraverse(dic, depth+1, node.left);
    if node.right: self.depthTraverse(dic, depth+1, node.right);
    

bt = BT();
# inp = [x for x in input().split()]
inp=[1,2,9,'N',3,4,5,2,1,3,'N','N']
arr=[];
for x in inp:
  try:
    arr.append(int(x));
  except:
    arr.append(x);
bt.insert(arr);
# bt.traverse()
dic={};
bt.depthTraverse(dic);
ans=[x for x in dic.values()];
if ans: print(*ans);

