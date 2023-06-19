def getAllAdj(i, j):
	M = len(arr)
	N = len(arr[0])
	adjNodes = []
	# left
	if j>0: adjNodes.append((i, j-1))
	# right
	if j<N-1: adjNodes.append((i, j+1))
	# top
	if i>0: adjNodes.append((i-1, j))
	# bottom
	if i<M-1: adjNodes.append((i+1, j))

	return adjNodes


def mark(i, j, marked, visited):
	if visited[i][j]:
		pass
	else:
		marked[i][j] = True
		visited[i][j] = True
		adj = getAllAdj(i, j)
		for i, j in adj:
			if arr[i][j] == "O":
				mark(i, j, marked, visited)

def main(M, N):
	marked = [[False]*N for i in range(M)]
	visited = [[False]*N for i in range(M)]
	
	for j in range(N):
		if not visited[0][j] and arr[0][j]=="O": 
			mark(0, j, marked, visited)
		if not visited[M-1][j] and arr[M-1][j]=="O": 
			mark(M-1, j, marked, visited)

	for i in range(1, M-1):
		if not visited[i][0] and arr[i][0]=="O": 
			mark(i, 0, marked, visited)
		if not visited[i][N-1] and arr[i][N-1]=="O": 
			mark(i, N-1, marked, visited)

	for i in range(M):
		for j in range(N):
			if not marked[i][j] and arr[i][j]=="O": arr[i][j]="X"
	
        


M, N = [int(x) for x in input().split()]
global arr
arr = [[x for x in input().split()] for i in range(M)]
main(M, N)
for x in arr:
	print (*x)
