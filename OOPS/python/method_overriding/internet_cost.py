class Cost:
  def Internet(self):
    pass
  
class AirtelSim(Cost):
  def __init__(self, cost):
    self.cost = cost
  def Internet(self):
    return self.cost
  
class VodafoneSim(Cost):
  def __init__(self, cost):
    self.cost = cost
    
  def Internet(self):
    return self.cost
  
class IdeaSim(Cost):
  def __init__(self, cost):
    self.cost = cost
  def Internet(self):
    return self.cost
  
A = AirtelSim(float(input()))
V = VodafoneSim(float(input()))
I = IdeaSim(float(input()))

print("AirtelSim Internet :", A.Internet())
print("VodafoneSim Internet :", V.Internet())
print("IdeaSim Internet :", I.Internet())
