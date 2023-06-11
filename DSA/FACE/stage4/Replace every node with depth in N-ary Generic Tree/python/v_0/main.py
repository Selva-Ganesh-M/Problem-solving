class Node:
  def __init__(self, data):
    self.data = data;
    self.children = [];

class GT:
  def __init__(self):
    self.root = None;

  def fill(self, arr, node=None):

    if not arr: return;
    
    # if not root or current node
    if not node:
      if not self.root: 
        self.root = Node(arr[0]);
        self.fill(arr[1:], self.root);
      return;

    # children
    try:
      children = arr[1:arr[0]+1];
    except IndexError:
      # no children exists to continue further
      return;

    # arr -> grand and future
    arr = arr[arr[0]+1:]

    grand_splited = []
    for i in range(len(children)):
      if not arr: break;
      grand_splited.append(arr[:arr[0]+1]);
      arr=arr[arr[0]+1:];

    # arr -> future
    for i in range(len(children)):
      child = Node(children[i]);
      node.children.append(child);
      if not grand_splited: continue;
      if grand_splited[i]==[0]: continue;
      current_grand_and_future = grand_splited[i];
      current_grand_and_future.extend(arr)
      self.fill(current_grand_and_future, child)

  def depth(self, depth=0, node=None):
    if not node:
      if self.root: 
        ans.append(depth)
        self.depth(depth+1, self.root);
      return;
    for x in node.children: ans.append(depth);
    for x in node.children:
        self.depth(depth+1, x);

global ans;
ans=[]
gt = GT();
N=input()
# gt.fill([3,3,1,2,3])
# gt.fill([3,3,1,2,3,2,11,12,0,0,2,8,9])
# gt.fill([3,3,1,2,3,2,11,12,1,1,2,8,9])
# gt.fill([2,4,1,2,3,4,0,0,0,0])
# n = input()
gt.fill([int(x) for x in input().split()])
gt.depth()
print(*ans)
