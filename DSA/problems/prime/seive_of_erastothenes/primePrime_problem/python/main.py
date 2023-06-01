import math

# To check whether the number is prime or not 
def isPrime(n: int):
  count = 0
  if n <= 1: return 0
  for i in range(1, math.floor(math.sqrt(n))+1):
    if (n % i == 0):
      count += 1
      if (n // i != i):
        count += 1
  return 1 if count == 2 else 0

# To find all the primes btw the given range(inclusive)
def rangePrimes(start, end):
  arr = [True] * (end+1)
  arr[0]=arr[1]=False
  for i in range(2, end+1):
    for j in range(i*i, end+1, i):
      if (arr[j]):
        arr[j]=False
  return [i for i in range(start, len(arr)) if arr[i]]

# prime prime
def primePrime(start, end):
  pp = 0
  for i in range(start, end+1):
    primes = rangePrimes(1, i)
    if isPrime(len(primes)):
      pp+=1
  return pp

print("Please enter the start and end values(inclusive): ")
print("eg. 3 10 -> 4")
[start, end] = [int(x) for x in input().split()]
print(primePrime(start, end))
