from abc import (
  ABC,
  abstractmethod,
abstractproperty
)

class Numbers:
  def __init__(self, n1, n2):
    self._n1 = n1
    self._n2 = n2


class Product(ABC):

  def __init__(self):
    pass
  
  @abstractmethod
  def findProduct(self):
    pass

class Calc(Numbers, Product):
  def __init__(self, n1, n2):
    Numbers.__init__(self, n1, n2)

  def findProduct(self):
    return self._n1 * self._n2

c = Calc(int(input()), int(input()))
print(c.findProduct())
    
