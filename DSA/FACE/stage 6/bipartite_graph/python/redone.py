from collections import deque
from typing import List

class Graph:
    def __init__(self, noOfVertices: int, edges: List[List[int]]):
        self.__noOfVertices: int = noOfVertices
        self._edges: List[List[int]] = edges
        self.adjList: List[List[int]] = [[] for i in range(noOfVertices+1)]
        for x, y in edges:
            if x > self.__noOfVertices or y > self.__noOfVertices: continue
            if x not in self.adjList[y]: self.adjList[y].append(x)
            if y not in self.adjList[x]: self.adjList[x].append(y)

    def biPartite(self)->List[int]:
        colors = [-1]*(self.__noOfVertices+1)
        visited = [False]*(self.__noOfVertices+1)
        def __biPartite(head):
            colors[head] = 1
            visited[head] = True
            queue = deque([
                [head, colors[head]],
                ])
            while (queue):
                currItem, currItemColor = queue.popleft()
                cColor = 1 if currItemColor == 2 else 2
                for rel in self.adjList[currItem]:
                    if not visited[rel]:
                        visited[rel] = True
                        colors[rel] = cColor
                        queue.append([rel, colors[rel]])
                    else:
                        if colors[rel] != cColor:
                            return False
            return True
                        
        for i in range(1, self.__noOfVertices + 1):
            if not visited[i]: 
                res = __biPartite(i)
                if not res: return [False, "IMPOSSIBLE"]
        return [True, colors[1:]]

            


noOfVertices, noOfEdges = list(map(int, input().split()))
edges = [[int(x) for x in input().split()] for i in range(noOfEdges)]
g = Graph(noOfVertices, edges)
[status, value] = g.biPartite()
if status:
    print(*value)
else:
    print(value)


# class Graph:
#   def __init__(self, noOfVertices, edges):
#     self.noOfVertices = noOfVertices
#     self.adjList = [[] for i in range(noOfVertices+1)]
#     for x, y in edges:
#       if x > self.noOfVertices or y > self.noOfVertices: continue
#       if y not in self.adjList[x]: self.adjList[x].append(y)
#       if x not in self.adjList[y]: self.adjList[y].append(x)
  
#   def isBipartite(self, src):
#     colors = [None]*(self.noOfVertices+1)
#     colors[0]=-1
#     colors[src] = 1
#     queue = [(src, 1)]
#     visited = [False]*(self.noOfVertices+1)
#     while (queue):
#       currQ = queue
#       queue = []
#       for node, pColor in currQ:
#         if not visited[node]: 
#           visited[node] = True
#           colors[node] = 1
#         for adjNode in self.adjList[node]:
#           if not visited[adjNode]:
#             visited[adjNode] = True
#             colors[adjNode] = 1 if pColor == 2 else 2
#             queue.append((adjNode, colors[adjNode]))
#           else:
#             if colors[adjNode] == pColor: return (False, colors[1:])
#       if not queue:
#         pendingArr = [i for i in range(len(visited)) if not visited[i] and i!=0]
#         if pendingArr: queue.append((pendingArr[0], 1))
#     return (True, colors[1:])
        
# pupil, noOfFriendships = list(map(int, input().split()))
# friendShips = [(int(x) for x in input().split()) for x in range(noOfFriendships)]

# graph = Graph(pupil, friendShips)
# src = 1
# status, colors = graph.isBipartite(src)
# if status:
#   print(*colors)
# else:
#   print("IMPOSSIBLE")