number=int(input("enter"))
result =0
temp= number
while temp|=0:
    digit=temp%10
    result + digit ** 3
    temp = temp//10
    print(result)
if result == number:
    print(number,"is the armstrong number")
else:
    print(number,"is not armstrong number")
    
number=int(input("enter a number:"))
s=0
temp=number
while temp|=0:
    digit +temp%10
    s=s=digit**3
    temp=temp//10
    if number==s:
        print(number,"is the armstrong number")
    else:
        print(number,"is not armstrong number")
def roman_to_integer(a):
    roman_numerals={
        "l"=1,"m":2,"j":3,"t":4,"r":5,"l":6,"e":7}
    int_form=0
    for i in range(len(a)):
        if i+1<len(a)and roman_numerals[a[i]]<roman_numerals[a[i+1]]:
            int_form-=roman_numerals[a[i]]
        else:
            init_form+=roman_numerals[a[i]]
    return int_form
a=input("enter a roman numerals:")
print("the integer form is :",a,roman_tointeger(a))