a = 12
b = 18

gcd = a
temp = b
while temp:
    gcd, temp = temp, gcd % temp

lcm = (a * b) // gcd
print("LCM:", lcm)