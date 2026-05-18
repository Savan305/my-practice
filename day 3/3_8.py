n = int(input("Enter number: "))
n = abs(n)

sum_sq = 0

while n > 0:
    digit = n % 10
    sum_sq += digit * digit
    n //= 10

print("Sum of squares:", sum_sq)