class Node:
  def __init__(self, data):
    self.data = data;
    self.right = None;
    self.left = None;

class Tree:
  def __init__(self):
    self.root = None;

  def __insert(self, node, data):
    if not node:
      return Node(data);
    if (data < node.data):
      node.left = self.__insert(node.left, data);
    else:
      node.right = self.__insert(node.right, data);
    return node;
  
  def insert(self, data):
    self.root = self.__insert(self.root, data);


  def __inOrder(self, node, arr):
    if not node:
      return;
    self.__inOrder(node.left, arr)
    arr.append(node.data)
    self.__inOrder(node.right, arr)
    
  def __preOrder(self, node, arr):
    if not node:
      return;
    arr.append(node.data)
    self.__preOrder(node.left, arr)
    self.__preOrder(node.right, arr)
  
  def __postOrder(self, node, arr):
    if not node:
      return;
    self.__postOrder(node.left, arr)
    self.__postOrder(node.right, arr)
    arr.append(node.data)
    
  def traverse(self):
    print("""Please select traversal methods:"
    1. Inorder
    2. Pre-order
    3. Post-order
    """)
    choice = input()
    ans=[]
    match choice:
      case "1":
        self.__inOrder(self.root, ans);
      case "2":
        self.__preOrder(self.root, ans)
      case "3":
        self.__postOrder(self.root, ans)
      case _:
        print("invalid choice. try again.");
        return;
    print(*ans)


tree = Tree()
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(9)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(8)
tree.traverse()
