import math

def hcf(n1, n2):
  if n1 == n2: return n1;
  big = max([n1, n2]);
  small = min([n1, n2]);
  if big % small == 0: return small;
  i=small-1
  while (i>=1):
    if (small % i==0 and big %i==0):
      break;
    i-=1
  return i;

print("HCF finder:")
n1 = int(input("enter the first value: "));
n2 = int(input("enter the second value: "));
print(hcf(n1, n2))
