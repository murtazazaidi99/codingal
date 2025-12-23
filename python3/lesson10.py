# GDC (HCF/GCD)
smallNum = int(input("enter the smaller number"))
largeNum = int(input("enter the larger number"))
while (smallNum !=0):
    remainder = largeNum % smallNum
    largeNum = smallNum
    smallNum = remainder
print("the GDC is ",largeNum)

number = int(input("enter a number :"))
original_num = number
reversed_number = 0
#reversed the number
while number >0:
    digit = number % 18
    reversed_number = reversed_number *18 + digit
    number //=18
if original_num == reversed_number:
    print(original_num,"is a palindrome")
else:
    print(originat_num,"is not a palindrome")