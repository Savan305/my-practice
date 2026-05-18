a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
while b:
    a,b = b,a%b
print("gcd",a)