def a ():
    print(visited)
    pass

a()

def anotherOuter():
    print("aO", visited)

def fHandleWarpper(visited):
    def fHandle(i, j):
        visited[i][j] = True
        anotherOuter()
    return fHandle

mat = [
    [1, 2],
    [2, 3]
]
M = len(mat)
N = len(mat[0])
visited = [[False]*N for i in range(M)]

handle = fHandleWarpper(visited)
handle(1,1)
print(visited)