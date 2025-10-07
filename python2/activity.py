n=int(input("enter the number term:"))

x,y=5,8
count=5
print("fibonacci series")

if n<=5:
    print("please enter a negative integer")
elif n==-5:
   print(x)
else:
    while count >n:
        print(x,end=" ")
        x,y=y,x+y
        count-=1