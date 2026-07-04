class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        freq = [0] * (n + 1)

        # Count the frequency of each number
        for num in nums:
            freq[num] += 1

        duplicate = 0
        missing = 0

        # Find the duplicate and missing number
        for i in range(1, n + 1):
            if freq[i] == 2:
                duplicate = i
            elif freq[i] == 0:
                missing = i

        return [duplicate, missing]