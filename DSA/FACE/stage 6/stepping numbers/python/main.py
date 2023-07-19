from collections import deque;




def handleItWrapper(mini, maxi, ans):
    def fHandleIt(num: int):
        queue = deque([num])
        while (queue):
            item = queue.popleft()
            if mini<=item<=maxi: ans.append(item)
            if item==0 or item>maxi: continue
            ld = item % 10
            sub = (item * 10) + (ld-1)
            add = (item * 10) + (ld+1)
            if ld==0:
                queue.append(add)
            elif ld==9:
                queue.append(sub)
            else:
                queue.append(sub)
                queue.append(add)
    return fHandleIt

def main(mini, maxi):
    ans = []
    handleIt = handleItWrapper(mini, maxi, ans)
    for i in range(0, 10):
        handleIt(i)
    return ans

# inp = [int(x) for x in input().split()]
# main(inp[0], inp[1])
ans = main(*[int(x) for x in input().split()])
ans.sort()
print(*ans)