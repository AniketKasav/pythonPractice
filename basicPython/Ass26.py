num = int(input("Enter a number: "))

sum = 0
product = 1

while num > 0:
    digit = num % 10

    sum = sum + digit
    product = product * digit

    num = num // 10

if sum == product:
    print("Spy Number")
else:
    print("Not a Spy Number")