def power(base,expo):
    if expo ==0:
        return 1
    else:
        return base * power(base,expo-1)
    
base  = int(input("enter the value of base:"))
expo = int(input("enter the value of expo:"))
print("power",power(base,expo))