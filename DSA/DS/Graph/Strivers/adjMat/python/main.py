
class Graph:   
	def __init__(self, noOfNodes, edges):
		self.noOfNodes = noOfNodes
		self.adjMat = [[False]*(self.noOfNodes+1) for i in range(noOfNodes+1)]
		for x, y in edges:
			self.adjMat[x][y] = True
			self.adjMat[y][x] = True
	def __str__(self):
        	return "\n".join(["{arr}".format(arr=arr) for arr in self.adjMat])
            
			


    
noOfNodes, noOfEdges = list(map(int, input().split()))
edges = []
for i in range(noOfEdges):
    edges.append(list(map(int, input().split())))
graph = Graph(noOfNodes, edges)
print(graph)


# # sample input // 1-based indexing
# 3 3
# 1 2
# 1 3
# 2 3
