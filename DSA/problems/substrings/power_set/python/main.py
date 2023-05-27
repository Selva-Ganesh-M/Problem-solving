
def substrings(s):
    arr = []
    for i in range((1<<len(s))-1):
        st=""
        for j in range(len(s)):
            if (i & (1<<j)):
                st+=s[j]
        arr.append(st)
    return arr

print(substrings("selva"))
