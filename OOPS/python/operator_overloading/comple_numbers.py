class Complex:
  def __init__(self, real, img):
    self.real = real
    self.img = img
  def __add__(self, other):
    return self.real + other.real, self.img + other.img
  
[r1, i1, r2, i2] = [int(x) for x in input().split()]
c1 = Complex(r1, i1)
c2 = Complex(r2, i2)
(r, i) = c1 + c2
print(r, "+ i"+str(i))
