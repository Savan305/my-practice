n = int(input("enter the number"))
even = 0
odd = 0
temp = n 
count = 0
while temp> 0:
    temp//=10
    count = count +1
for _ in range (count):
        digit = n%10
        if digit%2==0:
            even = even+1
        else:
            odd = odd +1
        n = n//10
    
print("even",even,"odd",odd)