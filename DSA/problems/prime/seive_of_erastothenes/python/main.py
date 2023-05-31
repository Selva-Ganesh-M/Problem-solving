import math

def primeGen(s, e):
    template = [x for x in range(s if s>2 else 2, e+1)]
    for i in range(2, math.floor(math.sqrt(e))+1):
        for j in range(len(template)):
            if (template[j]==i):
                continue
            if (template[j]!=0 and template[j]%i==0):
                template[j]=0
    return list(filter(lambda x: x!=0, template))
    
[s, e] = [int(x) for x in input().split()]
print(*primeGen(s, e))
