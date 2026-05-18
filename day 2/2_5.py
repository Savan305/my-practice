nums = list(map(int, input("Enter numbers: ").split()))

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)


# Enter numbers: 1 2 2 3 4 3 5
# List after removing duplicates: [1, 2, 3, 4, 5]