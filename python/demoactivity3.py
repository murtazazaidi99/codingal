num = int(input("Enter a number: "))

# Convert number to string to count digits
num_str = str(num)
power = len(num_str)

# Calculate sum of each digit raised to the power
total = sum(int(digit) ** power for digit in num_str)

# Check Armstrong condition
if total == num:
    print(f"{num} is an Armstrong number ")
else:
    print(f"{num} is NOT an Armstrong number ")