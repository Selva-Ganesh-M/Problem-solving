from collections import deque

class Graph:

  def __init__(self, noOfVertices, edges):
    self.noOfVertices = noOfVertices;
    self.edges = edges;
    self.adjList = [[] for i in range(noOfVertices + 1)]
    for x, y in edges:
      if x not in self.adjList[y]: self.adjList[y].append(x)
      if y not in self.adjList[x]: self.adjList[x].append(y)

  def bfs(self):
    ans = []
    visited = [False]*(self.noOfVertices+1);
    visited[0] = True
    def __bfs(src):
      queue = deque([src])
      while (queue):
        current = queue.popleft()
        if not visited[current]:
          visited[current] = True
          ans.append(current)
          for relative in self.adjList[current]:
            if not visited[relative]:
              queue.append(relative)
    for i in range(1, self.noOfVertices + 1):
      if not visited[i]: __bfs(i)
    return ans;

  def dfs(self):
    ans = []
    visited = [False]*(self.noOfVertices+1);
    visited[0] = True
    def __dfs(src):
      visited[src] = True
      ans.append(src)
      for relative in self.adjList[src]:
        if not visited[relative]:
          __dfs(relative)
      
    for i in range(1, self.noOfVertices + 1):
      if not visited[i]: __dfs(i)
    return ans;

      
# inp = [
#   [5,3],
#   [1,2],
#   [1,3],
#   [4,5],
# ]
# g = Graph(5, inp)

inp = [
  [4,5],
  [5,2],
  [2,6],
]
g = Graph(6, inp)
# bfs = g.bfs()
dfs = g.dfs()
print(*dfs)