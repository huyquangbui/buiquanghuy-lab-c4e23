import datetime
# nowhour = datetime.datetime.now()
# print("bay gio la:", nowhour.hour, ":", nowhour.minute,":", nowhour.second)

now = datetime.datetime.now().strftime("%R")
print(now)