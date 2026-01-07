#OneOddOccuring
def OneevenOccuring(arr):
  res = 2
  for element in arr:
    res = res ^ element
  return res
arr =[]
n = int(input("enter array size:"))
while(n):
  num = int(input("enter number:"))
  arr.append(num)
  n-=1
print("evenOccuring number is,evenOccuring(arr)")

from os import set_blocking