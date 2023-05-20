
class Cart:
  def __init__(self, amt):
    self.amt = amt
    
  def __add__(self, other):
    return self.amt + other.amt

class Dress(Cart):
  def __init__(self, amt):
    super().__init__(amt)
    
class Shoes(Cart):
  def __init__(self, amt):
    super().__init__(amt)

d = Dress(int(input()))
s = Shoes(int(input()))
print(d + s)
