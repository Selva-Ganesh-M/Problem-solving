import heapq

def main():
  N, K = list(map(int, input().split()));
  arr = list(map(int, input().split()));
  dic = {}
  for x in arr: dic[x] = 1 if x not in dic else dic[x]+1
  arr = [(-occ, key) for key, occ in dic.items() if key!=K];
  heapq.heapify(arr);
  KOriginal = KOcc = dic[K] if K in dic else 0;
  while True:
    maxOcc, maxValue = heapq.heappop(arr);
    maxOcc=abs(maxOcc);
    if KOcc > maxOcc:
      break;
    KOcc+=1;
    maxOcc -= 1
    heapq.heappush(arr, (-(maxOcc), maxValue));

  print(KOcc - KOriginal)
    
main()
