class Father:
  type = "father"
  def __init__(self, fName):
    self.fName = fName
    
class Mother:
  def __init__(self, mName):
    self.mName = mName
    
class Son(Father, Mother):
  def __init__(self, fName, mName, name):
    Father.__init__(self, fName)
    Mother.__init__(self, mName)
    self.name = name
    
  def getFamilyTree(self):
    print("Father is {}".format(self.fName))
    print("Mother is {}".format(self.mName))
    print("Son is {}".format(self.name))
    
    
kid = Son(input(), input(), input())
kid.getFamilyTree()
