num = int(input("Enter a three-digit number: "))

first = num // 100
last = num % 10

sum = first + last

print("Sum =", sum)