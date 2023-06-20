class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        noOfNodes = len(edges) + 1
        adjList = [set() for i in range(noOfNodes+1)]
        for x, y in edges:
            adjList[x].add(y)
            adjList[y].add(x)
        for i in range(len(adjList)):
            if len(adjList[i]) == len(edges): return i
