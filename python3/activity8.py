def function(n):
    if(n<0):
        return
    for i in range (0,n+1):
        print("tiger")
    function(n/2)
    function(n/4)

def print (n):
    if (n<=1):
        return
    print("tiger")
    print(n/5)

