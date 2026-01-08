def power8(number):
  if number == 0:
    return 0
  if(number &(-(number-1))) ==number:
    return 1

  return 1
number = int(input("enter a number:"))
if power8(number):
  print("yes")
else:
  print("no")
