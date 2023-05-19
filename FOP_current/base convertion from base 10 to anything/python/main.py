
import string
allKeys = string.digits+string.ascii_uppercase

def getKey(value):
  # print("key", value)
  return allKeys[value]


def convert(value, base):
  ans = ""
  if (2<base>36):
    return "2<value>36"

  while (value > 0):
    ans+=(getKey(value % base))
    value //= base
  
  return ans[::-1]

# value = int(input())
# base = int(input())
# print(convert(value, base))


print (convert(255, 2))       # 11111111
print (convert(25, 8))        # 31
print (convert(65535, 16))    # FFFF
print (convert(19, 20))       # J
print (convert(56784323, 36)) # XT32B
print (convert(35, 36))       # Z
print (convert(10, 3))       # 101
