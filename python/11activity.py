num=int(input("enter any number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("given number is not a prime number")
            break
    else:
      print("number is prime") 
else:
    print("please enter number greater then 1")       