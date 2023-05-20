class Cube:
  def __init__(self, side):
    self.side = side
    
class Area(Cube):
  def __init__(self, side):
    super().__init__(side)
    pass
  
  def getArea(self):
    area = (self.side**2)*6
    print("Area: {}".format(area))
    
class Volume(Cube):
  def __init__(self, side):
    super().__init__(side)
    pass
  
  def getVolume(self):
    volume = self.side**3
    print("Volume: {}".format(volume))
    
side = int(input())
area = Area(side)
area.getArea()
volume = Volume(side)
volume.getVolume()
