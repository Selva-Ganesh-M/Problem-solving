class Graph:
  def __init__(self, noOfNodes, edges):
    self.noOfNodes = noOfNodes;
    self.edges = [[] for i in range(noOfNodes)];
    self.__fill(edges);

  def __repr__(self):
    return "\n".join(["{}: {}".format(node, desties) for node, desties in enumerate(self.edges)])

  def __str__(self):
    return self.__repr__();

  def __fill(self, edges):
    for x, y in edges:
      self.edges[x].append(y);
      self.edges[y].append(x);

  def addEdge(self, edge):
    self.__fill([edge]);
    
  def removeEdge(self, edge):
    for idx, xEdge in enumerate(self.edges):
        if idx == edge[0]:
            self.edges[idx].remove(edge[1])
        if idx == edge[1]:
            self.edges[idx].remove(edge[0])
  
  


n = 3
edges = [
  (0, 1),
  (1, 2)
]
graph = Graph(n ,edges)
print(graph)
graph.addEdge((0,2))
print(graph)
graph.removeEdge((0,2))
print(graph)
      
