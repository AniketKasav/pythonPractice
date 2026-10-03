days = int(input("Enter number of days: "))

years = days // 365
remainingdays = days % 365

months = remainingdays // 30
remainingdays = remainingdays % 30

weeks = remaining_days // 7

print("Years =", years)
print("Months =", months)
print("Weeks =", weeks)