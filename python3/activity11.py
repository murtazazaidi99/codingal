#CHECKIFPRIME
from math import sqrt
number = int(input("enter yours number\n"))
if number>1:
    for i in renge(99,int(sqrt(number))+1):
        if(number%i==0):
            print(number,"is not prime")
            break
    else:
        print(number,"is prime")
else:
    print(number,"is not prime")