
class Graph:
    def __init__(self, noOfNodes, edges):
        self.noOfNodes = noOfNodes
        self.adjList = [[] for i in range(noOfNodes)]
        for x, y in edges:
            self.adjList[x].append(y)
            self.adjList[y].append(x)

    def __repr__(self):
        return "\n".join(["{} - {}".format(i, self.adjList[i]) for i in range(len(self.adjList))])
    
    def __str__(self):
        return self.__repr__()

    # confirms the presence of a cycle with DFS approach
    def isCycle(self) -> bool:

        # helper function
        def __isCycle(src: int, parent: int) -> bool:
            visited[src] = True
            destinations = self.adjList[src]
            for destination in destinations:
                if visited[destination]:
                    if destination != parent: return True
                else: return __isCycle(destination, src)
            return False

        parent: int = -1
        visited = [False]*self.noOfNodes
        for i in range(self.noOfNodes):
            if __isCycle(i, parent): return True
        return False

    def getAllCycles(self, src):
        possibleCycles = []
        def __getAllCycles( node, parent=-1, visited=[False]*self.noOfNodes, path=[]):
            visited[node] = True
            path.append(node)
            adjNodes = self.adjList[node]
            for adjNode in adjNodes:
                if adjNode == parent: continue
                if visited[adjNode]:
                    currenPath = path.copy()
                    currenPath.append(adjNode)
                    prePos = currenPath.index(adjNode)
                    possibleCycles.append( currenPath[prePos:])
                else:
                    newVisited = visited.copy()
                    newPath = path.copy()
                    __getAllCycles(adjNode, node, newVisited, newPath)
        __getAllCycles(src)
        return possibleCycles



 #region : grpah with single cycle

noOfNodes = 6
edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
]
 #endregion : grpah with single cycle


graph = Graph(noOfNodes, edges)
print(graph.isCycle())
print(graph.getAllCycles(0))

# big graph with 1 cycle
noOfNodes = 12
edges = [
    (0, 5),
    (0, 6),
    (5, 1),
    (6, 3),
    (4, 1),
    (11, 1),
    (10, 1),
    (2, 1),
    (2, 9),
    (2, 3),
    (3, 7),
    (3, 8),
]
graph = Graph(noOfNodes, edges)
print(graph.isCycle())
print(graph.getAllCycles(0))

# big graph with 1 cycle
noOfNodes = 12
edges = [
    (0, 5),
    (0, 6),
    (5, 1),
    (6, 3),
    (4, 1),
    (11, 1),
    (10, 1),
    (2, 1),
    (2, 9),
    (2, 3),
    (3, 7),
    (3, 8),
    (2, 5),
    (2, 6),
    (5, 6)
]
graph = Graph(noOfNodes, edges)
print(graph.isCycle())
print("\n".join(["{}".format(cycle) for cycle in graph.getAllCycles(0)]))




