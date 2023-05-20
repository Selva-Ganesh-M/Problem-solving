class Calculator:

  def simple_interest(self, p, n, r):
    return (p*n*r)/100

class SI(Calculator):
  def si(self, p, n, r):
    print('''Principle amount: {p}
No.Of.Years: {n}
Rate of interest: {r}'''.format(p=p, n=n, r=r))
    return self.simple_interest(p, n, r)

si = SI()
print("Simple Interest:", si.si(int(input()), int(input()), int(input())))
