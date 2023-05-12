def rotate(s, turns):
    ans=""
    for i in range(turns):
        last = s[-1];
        s=last+s[:len(s)-1]
        print("for iteration => s =>", s);
    return s

[s, turns]=[x for x in input("Enter the string and number of rotations: ").split()]
print(rotate(s, int(turns)))
