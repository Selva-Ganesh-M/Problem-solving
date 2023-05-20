class Customer:

  def __init__(self, ac_no):
    self.__ac_no = ac_no;
    self.getAccountNumber();
    self.__processAccount()

  def getAccountNumber(self):
    print("Customer Account Number :",self.__ac_no)
  
  def __processAccount(self):
    lis = []
    while (True):
      inp = input()
      if (inp=="-1"):
        break
      lis.append(inp)
    print("Processing Account") if self.__ac_no in lis else print("Account Not Found")

cus = Customer(input())
