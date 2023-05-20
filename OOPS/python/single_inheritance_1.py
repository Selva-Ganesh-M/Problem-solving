class Player:
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score

class Game(Player):
  def __init__(self, name, age, score):
    Player.__init__(self, name, age, score)
    
  def calcPercent(self):
    print("%.1f" % (self.score/10))

  def getDetails(self):
    print(self.name+" "+str(self.age))

game = Game(input(), int(input()), int(input()))
game.getDetails()
game.calcPercent()
    
