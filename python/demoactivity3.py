num = int(input("Enter a number: "))
num_str = str(num)
power = len(num_str)

total = sum(int(digit) ** power for digit in num_str)
if total == num:
    print(f"{num} is an Armstrong number ")
else:
    print(f"{num} is NOT an Armstrong number ")