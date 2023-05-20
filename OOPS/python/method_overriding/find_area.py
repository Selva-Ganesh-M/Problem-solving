

class Rectangle:
  def __init__(self, length, breadth):
    self._length = length
    self._breadth = breadth

  @property
  def getLength(self):
    return self._length

  @property
  def getBreadth(self):
    return self._breadth

  def area(self):
    return self._breadth * self._length

class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)

  def area(self):
    return self._breadth ** 2

rect = Rectangle(int(input()), int(input()))
print("Area of Rectangle:",rect.area())

square = Square(int(input()))
print("Area of Square:",square.area())
