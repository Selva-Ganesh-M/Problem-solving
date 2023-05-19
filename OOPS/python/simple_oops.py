
#Type your code here...

class Mobile:
  def __init__(self, owner, brand, color, pixel):
    self.__owner = owner
    self.__brand = brand
    self.__color = color
    self.__pixel = pixel
    
  def display(self):
    # print(f"{self.__owner} own {self.__brand} {self.__color} color smartphone having {self.__pixel} MP camera")
    print("{owner} own {brand} {color} color smartphone having {pixel} MP camera".format(owner = self.__owner, brand = self.__brand, color = self.__color, pixel = self.__pixel))

    
owner = input()
brand = input()
color = input()
pixel = int(input())

mobile = Mobile(owner, brand, color, pixel)
mobile.display()
