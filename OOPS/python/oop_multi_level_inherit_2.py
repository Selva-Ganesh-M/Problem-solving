class Stud1:
  def __init__(self, s1_paid):
    self.s1_paid = s1_paid


class Stud2:
  def __init__(self, s2_paid):
    self.s2_paid = s2_paid


class Fee(Stud1, Stud2):
  def __init__(self, totalFee, s1_paid, s2_paid):
    self.totalFee = totalFee
    Stud1.__init__(self, s1_paid)
    Stud2.__init__(self, s2_paid)

  def getDue(self):
    ans = self.totalFee - (self.s1_paid + self.s2_paid)
    print("The amount they need to arrange: {}".format(ans))
    

fee = Fee(int(input()), int(input()), int(input()))
fee.getDue()
