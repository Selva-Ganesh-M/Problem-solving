class Node:
  def __init__(self, data):
    self.data = data;
    self.parent = None;
    self.left = None;
    self.right = None;

class BSTIterator:
  def __init__(self):
    self.root = None;
    self.iter = None;
    self.inOrderList = [];

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
        node.left.parent = node;
    else:
      if node.right:
        self.fill(data, node.right);
      else:
        node.right = Node(data);
        node.right.parent = node;

  def __fixIter(self, value=-2147483647, node=None):
    if not node:
      if not self.root: return None;
      return self.__fixIter(value, self.root);
    if not node.left:
      node.left = Node(value);
      node.left.parent = node
      self.iter = node.left;
      return;
    self.__fixIter(value, node.left);

  def __hasNext(self):
    if self.iter in self.inOrderList:
      pos = self.inOrderList.index(self.iter)
      return True if pos != len(self.inOrderList)-1 else False

  def inOrder(self, node=None):
    if not node:
      if self.root: return self.inOrder(self.root);
      return;
    if node.left: self.inOrder(node.left)
    self.inOrderList.append(node)
    if node.right: self.inOrder(node.right)
      
  def __next(self):
    if self.iter in self.inOrderList:
      pos = self.inOrderList.index(self.iter)
      if pos != len(self.inOrderList)-1:
        self.iter = self.inOrderList[pos+1];
        return self.iter.data;
      return "no next item"
    
        

  def handleIterQueries(self, queries):
    if not self.root: return []
    self.__fixIter();
    self.inOrder();
    ansArr=[]
    for query in queries:
        if query == "next":
          ansArr.append(self.__next());
        elif query == "hasNext":
          ansArr.append(self.__hasNext());
        else :
          print("invalid choice");
    return ansArr

tree = BSTIterator();
# n=input()
# arr=[int(x) for x in input().split()]
arr=[7, 3, 15, 9, 20];
for x in arr: tree.fill(x);
# queries=[x for x in input().split()]
queries = ["next", "next", "hasNext", "next", "next", "next", "hasNext"]
print(*tree.handleIterQueries(queries))
