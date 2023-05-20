class Number:
  def __init__(self, number):
    self.number = number
    
class Neon(Number):
  def __init__(self, number):
    Number.__init__(self, number)
    
  def isNeon(self):
    num = self.number
    sq = num**2
    ans = 0
    while (sq):
      rem = sq % 10
      ans+=rem
      sq//=10
    return num == ans
  
num = Neon(int(input()))
sol = "Neon" if num.isNeon() else "Not Neon"
print(sol)
