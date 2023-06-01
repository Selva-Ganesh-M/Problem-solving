def seive(n):
    arr = [True]*10000000;
    arr[0]=arr[1]=False
    ans=[]
    for i in range(2, len(arr)):
        if (arr[i]):
            ans.append(i)
            if len(ans)==n:
                break
        for j in range(i*i, len(arr), i):
            if arr[j]:
                arr[j]=False
    return ans[-1]
print(seive(int(input("Enter the nth prime you want: "))))
