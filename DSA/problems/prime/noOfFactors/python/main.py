import math

def factors(n : int):
    factor_count = 0
    for i in range(1, math.floor(math.sqrt(n))+1):
        if n % i ==0:
            factor_count+=1
            if (n//i)!=i:
                factor_count+=1
    return factor_count
    
print(factors(int(input("Enter the value to find factors: "))))
