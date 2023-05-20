#Type code here...
import math

class Circle:
  def __init__(self, r):
    self.radius = r
    
  def __add__(self, other):
    return self.radius + other.radius
  
  def area(self):
    return math.pi * self.radius**2
  
c1 = Circle(int(input()))
c2 = Circle(int(input()))
print(c1.radius)
print(c2.radius)
print("Radius of Two Circle:", c1 + c2)
print("Area:", c1.area()+c2.area())
