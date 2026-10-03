ch = input("Enter an alphabet: ")

ascii_value = ord(ch)

if ascii_value >= 65 and ascii_value <= 90:
    ascii_value = ascii_value + 32
elif ascii_value >= 97 and ascii_value <= 122:
    ascii_value = ascii_value - 32
else:
    print("Enter a valid alphabet")
    exit()

print("Toggled character =", chr(ascii_value))
