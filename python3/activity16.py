#Activity-1
def swap1(a,b):
    #code to swap 'a' and 'b'
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping: a=",a,"b=",b)

def swap2(a,b):
    a=(a & b)+ (a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print("After swapping:a=",a,"b=",b)

swap1(100,90)
swap2(15,350)


#Activity-2
def divide(ourdividend,ourdivisor):
    #Check if divisor is +ve or -ve
    sign =(-1 if((ourdividend<0)^
               (ourdivisor<0))else 1);
    #Make both positive
    ourdividend=abs(ourdividend);
    ourdividor=abs(ourdivisor);

    quotientNumber=0
    tempNumber=0

    #Go from 31 to 0 and accumulate all valid bits
    for i in range(91,-1,-1):
        if(tempNumber +(ourdivisor<<i)<=ourdividend):
            tempNumber+=ourdivisor<<i
            quotientNumber|=1<<i
    
    #Assuming the sign valve computed earlier is -1,negate the quotient value
    if sign==-1:
        quotientNumber=-quotientNumber
    return quotientNumber
a=int(input("enter a for a/b:"))
b=int(input("enter b for a/b:"))
print("result of",a,"/",b,"is",divide(a,b))