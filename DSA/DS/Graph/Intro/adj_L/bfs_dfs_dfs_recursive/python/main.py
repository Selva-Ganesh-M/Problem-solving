
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

    def __search_success_msg(self, src, target, level):
        return """
{} is found {} levels down {}
        """.format(target, level, src)
    
    def __search_failure_msg(self, target):
        return "{} is not found".format(target)

    def bfs(self, src, target):
        level = 0
        if src == target:
            return level
        visited = [False] * self.noOfNodes
        visited[src] = True
        queue = [src]
        while queue:
            currQ = queue
            queue = []
            for node in currQ:
                arr = self.adjList[node]
                for desti in arr:
                    if not visited[desti]:
                        if desti == target: return self.__search_success_msg(src, target, level+1)
                        visited[desti] = True
                        queue.append(desti)
            level+=1
        return self.__search_failure_msg(target)

    def dfs(self, src):
        callStack = [src]
        ans = [src]
        visited = [False] * self.noOfNodes
        visited[src] = True
        while callStack:
            currNode = callStack.pop()
            if not visited[currNode]: ans.append(currNode)
            visited[currNode] = True
            for desti in self.adjList[currNode][::-1]:  
                if not visited[desti]: callStack.append(desti)
        print("""dfs is: {}""".format(ans))

    def dfs_recursive(self, src):
        ans = []
        visited = [False]*self.noOfNodes
        def __dfs_recursive(src):
            ans.append(src)
            visited[src] = True
            currNode = src
            currDesti = self.adjList[currNode]
            for desti in currDesti:
                if not visited[desti]:
                    visited[desti] = True
                    __dfs_recursive(desti)
        __dfs_recursive(src)
        print("dfs recursive:", ans)


noOfNodes = 6
edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
]
graph = Graph(noOfNodes, edges)
print(graph)
srcRes = graph.bfs(2, 4)
print(srcRes)
graph.dfs(0)
graph.dfs_recursive(0)

