def printnumber(n):
    literation = 0 
    print("total number entered my user",n)
    literation+=1
    print("total literation done by computer ",literation,"\n")
printnumber(30)
printnumber(1000)
print("\n with any 'n' the time taken by computer will not change ")


def OnTime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("when n is ",n,"iteration =",iteration)

OnTime(4)
OnTime(20)
OnTime(67)
OnTime(98)
OnTime(1987)


def test(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            iteration+=1
            print("")
            print("\n when n is ",n,"iteration =",iteration)
test(7)
test(8)
test(9)
test(10)
test(11)