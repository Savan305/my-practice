nums = list(map(int, input("Enter numbers: ").split()))

largest = second = float('-inf')

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest:", second)


#Enter numbers: 10 20 5 8 25
# Second Largest: 20