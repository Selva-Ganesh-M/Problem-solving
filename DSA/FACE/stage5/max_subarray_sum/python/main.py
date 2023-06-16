n, start, end = list(map(int, input().split()));
arr = list(map(int, input().split()));
ans = [];
max = 0


for i in range(len(arr)-start+1):
  if ans:
    remIndex = i-1;
    addIndex = i+start-1;
    prevQItem = ans[-(end-start+1)]
    newItem = prevQItem - arr[remIndex] + arr[addIndex];
    ans.append(newItem)
  else:
    ans.append(sum(arr[:start]));
  if ans[-1] > max: max = ans[-1]
  for j in range(i+start, i+end):
    if j < n: 
      ans.append(ans[-1]+arr[j]);
      if ans[-1] > max: max = ans[-1]
    


print(max)
