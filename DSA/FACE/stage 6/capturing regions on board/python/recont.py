from typing import List

def getRelatives(i, j):
    relatives = []
    try:
        if mat[i-1][j]: relatives.append((i-1, j))
    except: pass
    try:
        if mat[i+1][j]: relatives.append((i+1, j))
    except: pass
    try:
        if mat[i][j-1]: relatives.append((i, j-1))
    except: pass
    try:
        if mat[i][j+1]: relatives.append((i, j+1))
    except: pass
    return relatives

def handleWrapper(mat, marks, visited):
    def fHandle(i, j):
        visited[i][j] = True
        marks[i][j] = True
        relatives = getRelatives(i, j)
        for x, y in relatives:
            if not visited[x][y] and mat[x][y]=="O":
                fHandle(x, y)

    return fHandle


def main(mat: List[List[int]]):
    M = len(mat)
    N = len(mat[0])
    marks = [[False]*N for i in range(M)]
    visited = [[False]*N for i in range(M)]
    handle = handleWrapper(mat, marks, visited)

    # left -> right
    for j in range(N):
        if not visited[0][j] and mat[0][j]=="O":
            handle(0, j)
        if not visited[M-1][j] and mat[M-1][j]=="O":
            handle(M-1, j)
    
    # top -> down
    for i in range(1, M-1):
        if not visited[i][0] and mat[i][0]=="O":
            handle(i, 0)
        if not visited[i][N-1] and mat[i][N-1]=="O":
            handle(i, N-1)

    marks = [["O" if marks[i][j] else "X" for j in range(N)] for i in range(M)]
    for x in marks:
        print(*x)
m, n = list(map(int, input().split()))
mat = [
    [x for x in input().split()] for i in range(m)
]
main(mat)



# def getAllAdj(i, j):
# 	M = len(arr)
# 	N = len(arr[0])
# 	adjNodes = []
# 	# left
# 	if j>0: adjNodes.append((i, j-1))
# 	# right
# 	if j<N-1: adjNodes.append((i, j+1))
# 	# top
# 	if i>0: adjNodes.append((i-1, j))
# 	# bottom
# 	if i<M-1: adjNodes.append((i+1, j))

# 	return adjNodes


# def mark(i, j, marked, visited):
# 	if visited[i][j]:
# 		pass
# 	else:
# 		marked[i][j] = True
# 		visited[i][j] = True
# 		adj = getAllAdj(i, j)
# 		for i, j in adj:
# 			if arr[i][j] == "O":
# 				mark(i, j, marked, visited)

# def main(M, N):
# 	marked = [[False]*N for i in range(M)]
# 	visited = [[False]*N for i in range(M)]
	
# 	for j in range(N):
# 		if not visited[0][j] and arr[0][j]=="O": 
# 			mark(0, j, marked, visited)
# 		if not visited[M-1][j] and arr[M-1][j]=="O": 
# 			mark(M-1, j, marked, visited)

# 	for i in range(1, M-1):
# 		if not visited[i][0] and arr[i][0]=="O": 
# 			mark(i, 0, marked, visited)
# 		if not visited[i][N-1] and arr[i][N-1]=="O": 
# 			mark(i, N-1, marked, visited)

# 	for i in range(M):
# 		for j in range(N):
# 			if not marked[i][j] and arr[i][j]=="O": arr[i][j]="X"
	
        


# M, N = [int(x) for x in input().split()]
# global arr
# arr = [[x for x in input().split()] for i in range(M)]
# main(M, N)
# for x in arr:
# 	print (*x)