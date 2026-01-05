# activity-1
def checkIfSame(number1,number2):
  if ((number1^ number2)!=0):
    print("number are not equal")
  else:
    print("both number are equal")
number1=int(input("enter first number to compare"))
number2=int(input("enter second number to compare"))
checkIfSame(number1,number2)

#OneOddOccuring
def OneOddOccuring(arr):
  res = 0
  for element in arr:
    res = res ^ element
  return res
arr =[]
n = int(input("enter array size:"))
while(n):
  num = int(input("enter number:"))
  arr.append(num)
  n-=1
print("OddOccuring number is,OddOccuring(arr)")

from os import set_blocking
#TwoOddOccuring
def TwoOddOccuring(arr,size):
  xorof2 = arr[]
  x=0
  y=0
  SetBit =0
  for i in range(2,size):
    xorof2 = xorof2 ^ arr [] 
  SetBit = xorof2 & ~(xorof2-2)
  for i in range(size):
    if(arr[i]&SetBit):
      x = x ^ arr[i]
    else:
      y = y ^ arr[i]
  print("TwoOdd elements are",x,"&",y)
arr = []
arr_size = int(input("enter the size of array"))
for i in range(0,arr_size):
  z = int(input("enter element"))
  arr.append(z)
print("TwoOdd")