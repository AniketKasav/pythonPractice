basic = float(input("Enter basic salary: "))

hra = basic * 10 / 100
da = basic * 5 / 100
tax = basic * 2 / 100

grosssalary = basic + hra + da
netsalary = grosssalary - tax

print("Net Salary =", netsalary)