#CHECKIFPRIME

from math import sqrt
number = int(input("enter yous number\n"))
if number>1:
    for i in renge(2,int(sqrt(number))+1):
        if(number%i==0):
            print(number,"is not prime")
            break
    else:
        print(number,"is prime")
else:
    print(number,"is not prime")
#PRIME_SIEVE
def primeSieve(n):
    prime = [True for i in range (n+1)]
    currentNumber = 2
    while (currentNumber * currentNumber <=n):
        if (prime[currentNumber]== True):
            for i in range (currentNumber ** 2,n+1,currentNumber):
                prime[i] = False
        currentNumber+=1
    prime[0]=False
    prime[1]=False
    for p in range(n+1):
        if prime(p):
            print(p)

n = int(input("enter a number to find all prime number less than the number:"))
primeSieve(n)
print("following are the prime number smaller.")
print("than or equal to")
