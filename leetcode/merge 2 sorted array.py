num1 = [1,3,5]
num2 = [2,4,6]
idx = 0
n = len(num1)
m = len(num2)
res = [0]*(n+m)
i = 0
j = 0   
while i<n and j<m:
    if num1[i]<num2[j]:
        res[idx] = num1[i]
        i+=1    
    else:
        res[idx] = num2[j]
        j+=1
    idx+=1
while i<n:
    res[idx] = num1[i]
    idx+=1
    i+=1
while j<n:
    res[idx] = num2[j]
    idx+=1
    j+=1
print(res)