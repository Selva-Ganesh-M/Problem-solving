class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        adjNodes = [set() for i in range(n)]
        for x, y in edges:
            adjNodes[x].add(y)
            adjNodes[y].add(x)
        visited = [False]*n
        queue = [source]
        visited[source] = True
        while (queue):
            node = queue[0]
            if node == destination: return True
            queue = queue[1:]
            visited[node] = True
            for adjNode in adjNodes[node]:
                if not visited[adjNode]:
                    queue.append(adjNode)
                    visited[adjNode] = True
        return False
