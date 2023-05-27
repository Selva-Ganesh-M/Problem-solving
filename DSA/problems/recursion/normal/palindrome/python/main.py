def palindrome(s, i):
    n=len(s)
    if (i>n//2):
        return True
    return palindrome(s, i+1) if s[i]==s[n-i-1] else False
    
print(palindrome("abcdeedcba", 0))
