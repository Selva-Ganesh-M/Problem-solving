def lcm(n1, n2):
  if n1==n2: return n1;
  greater = max([n1, n2])
  lesser = min([n1, n2])
  if greater % lesser==0: return greater;
  i = 1
  while (True):
    val = greater * i;
    if val % lesser == 0:
      break;
    i+=1;
  return greater * i;


n1 = int(input("Enter the first value: "))
n2 = int(input("Enter the second value: "))
print(lcm(n1, n2))
