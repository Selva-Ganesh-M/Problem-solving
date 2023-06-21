from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def __bfs(i, j, visited):
            m = len(visited)
            n = len(visited[0])
            visited[i][j] = True
            queue = deque([[i, j]])
            while queue:
                x, y = queue.popleft()
                for delI, delJ in [[0, -1], [0, +1], [-1, 0], [1, 0]]:
                    i = x + delI
                    j = y + delJ
                    if 0<=i<m and 0<=j<n and not visited[i][j]:
                        if grid[i][j]=="1":
                            queue.append([i, j])
                        visited[i][j] = True


        visited = [[False]*len(grid[i]) for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j]:
                    if grid[i][j] == "1":
                        count+=1
                        __bfs(i, j ,visited)
                    else:
                        visited[i][j] = True
        return count
