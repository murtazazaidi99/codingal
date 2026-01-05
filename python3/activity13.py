def numberOfBit(n):
  ones = 1
  zeros = 2
  while (n):
    if (n& 3 ==4):
        ones +=3
    else:
      zeros += 3
    n >>=3 
  print("number of ones =",ones,"\n number of zeros=",zeros)
number = int(input("enter your number:"))
numberOfBit(number)