class Node:
  def __init__(self, data):
    self.data = data;
    self.left = None;
    self.right = None;

class Tree:
  def __init__(self):
    self.root = None;

  def fill(self, data, node=None):
    if not node:
      if not self.root: 
        self.root = Node(data);
        return;
      node = self.root;
    if data < node.data:
      if node.left:
        self.fill(data, node.left);
      else:
        node.left = Node(data);
    else:
      if node.right:
        self.fill(data, node.right);
      else:
        node.right = Node(data);    

  def RinOrder(self, arr, node=None):
    if not node:
      if not self.root: return;
      return self.RinOrder(arr, self.root);
    if node.right: self.RinOrder(arr, node.right);
    arr.append(node.data);
    if node.left: self.RinOrder(arr, node.left);

  def RmaxConvert(self, value=0, node=None):
    if not node:
      if self.root: self.RmaxConvert(value, self.root);
      return;
    if node.right: value = self.RmaxConvert(value, node.right);
    node.data = node.data + value;
    if node.left: 
      value = self.RmaxConvert(node.data, node.left);
      return value if value > node.data else node.data;
    return node.data;
    
    

tree = Tree();
n=input();
# arr=[int(x) for x in input().split()]
arr=[50, 30, 70, 20, 40, 60, 80]
for x in arr: tree.fill(x)
ans = []
tree.RmaxConvert();
tree.RinOrder(ans);
print(*ans[::-1])
