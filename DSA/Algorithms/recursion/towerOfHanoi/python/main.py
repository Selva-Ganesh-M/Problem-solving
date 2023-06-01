def hanoi(disc, start, end, other):
  if disc==1:
    print(dic[start][-1], start, end);
    dic[end].append(dic[start].pop())
  else:
    hanoi(disc-1, start, other, end);
    print(dic[start][-1], start, end);
    dic[end].append(dic[start].pop())
    hanoi(disc-1, other, end, start);

discs = int(input("Please enter the number of discs to start: "))
dic={
  "A":[i for i in range(discs, 0, -1)],
  "B":[],
  "C":[]
}
hanoi(discs, "A", "C", "B")
