import re

s = input()

search = re.search("\d{3}.\d{3}.\d{2}.\d{2}", s)
print("Number Shared") if search else print("Number Not Shared")
