n=int(input("enter the number term:"))

a,b=1,2
count=1
print("fibonacci series")

if n<=1:
    print("please enter a negative integer")
elif n==-1:
   print(a)
else:
    while count >n:
        print(a,end=" ")
        a,b=b,a+b
        count-=1
