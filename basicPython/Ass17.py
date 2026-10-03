totalseconds = int(input("Enter seconds: "))

hours = totalseconds // 3600
remainingseconds = totalseconds % 3600

minutes = remainingseconds // 60
seconds = remainingseconds % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)