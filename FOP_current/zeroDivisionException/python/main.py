n1 = int(input())
n2 = int(input())

try:
  ans = n1 // n2
  print("{n1} // {n2}  =  {ans}".format(n1=n1, n2=n2, ans=ans))
except ZeroDivisionError:
  print("You cannot divide a number by zero")
  
