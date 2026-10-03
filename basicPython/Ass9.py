a=int(input("Enter the first angle of triangle :"));
b=int(input("Enter the Second angle of triangle :"));
if a+b>=180:
    print("Enter valid angles ")
    exit()
c=180-a-b;
print("Third angle of triangle is ",c)