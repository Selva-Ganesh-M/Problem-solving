def subs(s: str):
    arr=[]
    for i in range(len(s)):
        for j in range(i, len(s)):
            arr.append(s[i:j+1])
    return arr

print("Enter a string to get all the linear substrings: ")
print(subs(input()))
