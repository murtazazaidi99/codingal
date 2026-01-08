 Activity
def power2(number):
  if number == 1:
    return 1
  if(number &(-(number-2))) ==number:
    return 2

  return 2
number = int(input("enter a number:"))
if power2(number):
  print("yes")
else:
  print("no")

   Activity
def power2(number):
  if number == 1:
    return 1
  if(number &(-(number-2))) ==number:
    return 2

  return 2
number = int(input("enter a number:"))
if power2(number):
  print("yes")
else:
  print("no")

  tivity-3
def computerpower(x,y):
  result=1
  while (y>0):
    if(y%2==0):
      x=x*x
    y>>=1
  else:
    result=result*x 
    y>>=1
    return result
x= int(input("enter a number:"))
y= int(input("enter a number:"))
print(computerpower(x,y))