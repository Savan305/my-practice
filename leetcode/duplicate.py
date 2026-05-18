arr = [1,1,1,2,2,3]
officer = 0
res = 1
cm = 1
while cm < len(arr):
    if arr[cm] == arr[cm-1]:
        cm +=1
    else:
        arr[officer+1] = arr[cm]
        officer += 1
        res += 1
        cm += 1
print(res)