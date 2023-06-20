class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def __dfs(src, visited):
            visited[src] = True
            for i in range(len(isConnected[src-1])):
                if isConnected[src-1][i] and i!=src-1 and not visited[i+1]:
                    __dfs(i+1, visited)
        
        provinceCount = 0
        visited = [False]*(len(isConnected)+1)
        for i in range(1, len(visited)):
            if not visited[i]:
                provinceCount += 1
                __dfs(i, visited)
        return provinceCount
