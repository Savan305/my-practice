class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = []

        for i in range(len(numbers)):
            arr.append((numbers[i], i))

        arr.sort()

        left = 0
        right = len(arr) - 1

        while left < right:
            sums = arr[left][0] + arr[right][0]

            if sums == target:
                return [arr[left][1] + 1, arr[right][1] + 1]

            elif sums > target:
                right -= 1

            else:
                left += 1

        return []