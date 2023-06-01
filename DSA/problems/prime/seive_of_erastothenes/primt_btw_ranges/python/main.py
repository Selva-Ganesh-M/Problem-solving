def seive(start, end):
  arr = [True] * (end+1);
  arr[0]=arr[1]=False;
  for i in range(2, end+1):
    for j in range(i*i, end+1, i):
      if arr[j]:
        arr[j] = False
  return [i for i in range(start, end+1) if arr[i]]
      

cases = int(input("Enter the number of test cases: "))
for i in range(cases):
  print("Enter the range x and y to find primes (inclusive): ")
  print("eg.1 10")
  start, end = [int(x) for x in input().split()]
  print(start, end)
  print(*seive(start, end))
  print("\n")
