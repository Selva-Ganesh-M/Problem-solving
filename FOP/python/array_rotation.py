
# size of the input array
size = input();

#space seperated list items
arr = [x for x in input().split()]

#number of rotations
turns = int(input())

# rotating the array
for i in range(turns):
  last = [];
  last.append(arr[-1])
  last.extend(arr[:len(arr)-1]);
  arr=last
print(*arr)
