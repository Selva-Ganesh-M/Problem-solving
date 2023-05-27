def backtracking(i, N):
    if (i>N):
        return
    backtracking(i+1, N);
    print(i)

n = int(input("Enter to value to print: "))
backtracking(1, n)
