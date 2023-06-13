class Node:
  def __init__(self, data, respect):
    self.data = data;
    self.respect = respect;
    self.children = [];

class NaryTree:
  def __init__(self):
    self.root = None;
    self.cutOffQueue = None;

  def __traverse(self, node = None):
    queue = [];
    if not self.root: return;
    if not node: 
      node = self.root;
    queue = [node];
    while (queue):
      currQ = queue;
      queue = []
      for item in currQ:
        queue.extend(item.children);
    pass
  
    
  
  def __fillQ(self, num: int):
    return [Node(i, None) for i in range(1, num+1)]

  def __lectureQ(self, queue, arr):
    for idx, [parentData, respect] in enumerate(arr, start = 1):
      if parentData == -1:
        self.root = queue[idx-1];
        continue;
      queue[parentData-1].children.append(queue[idx-1]);
      queue[idx-1].respect = respect;
  
  def __getRespect(self):
    if not self.root: return;
    arr = []
    def __i_main(node):
      childRespect = 1;
      for child in node.children:
        if child.respect == 0: childRespect = 0
        __i_main(child);
      if node.respect == 1 and (not node.children or childRespect == 1):
        arr.append(node.data)
    __i_main(self.root);
    return arr;
  
  def payRespect(self, arr: [[int, int]]) -> [int]:
    queue = self.__fillQ(len(arr));
    self.__lectureQ(queue, arr);
    self.__traverse();
    respectQueue = self.__getRespect();
    respectQueue.sort();
    print(*respectQueue) if respectQueue else print(-1)
    pass 

nt = NaryTree();

# # real run
# arr = []
# for i in range(int(input())):
#   arr.append([int(x) for x in input().split()])
# nt.payRespect(arr)


# test run
# # testrun1
# arr = [
#   [2,1],
#   [-1,0],
#   [1,0],
#   [1,1],
#   [1,1],
#   [4,0],
#   [5,1],
#   [7,0],
# ]
# nt.payRespect(arr)


# # testrun 2
# arr = [
#   [-1, 0],
#   [1, 1],
#   [1, 1],
#   [2, 0],
#   [3, 0],
# ]
# nt.payRespect(arr)

# testrun 3
arr = [
  [3, 1],
  [1, 1],
  [-1, 1],
  [2, 1],
  [3, 0]
]
nt.payRespect(arr)
