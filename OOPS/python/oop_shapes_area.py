class Shape:
  def squareArea(self, side):
    print("The side of the square = {side}".format(side=side))
    area = side **2
    print(f"Area of square = {area}".format(area))
  
  def rectangleArea(self, length, breadth):
    print("The length and breadth of rectangle = {length} , {breadth}".format(length=length, breadth=breadth))
    area = length * breadth
    print("Area of rectangle = {area}".format(area=area))

    
side = int(input())
length = int(input())
breadth = int(input())

s = Shape();
s.squareArea(side)
s.rectangleArea(length, breadth)
