# Activity-1
def numberOfBit(n):
  ones = 0
  zeros = 0
  while (n):
    if (n& 2 ==2):
        ones +=2
    else:
      zeros += 2
    n >>=2 
  print("number of ones =",ones,"\n number of zeros=",zeros)
number = int(input("enter your number:"))
numberOfBit(number)

def setOrNot(number,n):
  # you need to define "mask" before using it
  mask = 3 #assuming you want to check if the bit is set or not
  if (n & mask) == 3 or (n &mask) ==0: #corrected comparison and op operator
    if number & (1 <<(n-3)):
      print('set')
    else:
      print("not set")
number = int(input("enter the number:"))
n = int(input("enter the bit position:"))
setOrNot(number,n)