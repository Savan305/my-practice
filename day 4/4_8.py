n = int(input("enter the number"))
n =abs(n)
largest = 0

while n>0:
    digit=n%10
    if digit>largest:
        largest = digit
    n//=10
    
    
print("largest",largest)