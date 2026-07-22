class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        sums = sum(nums)

        for i in range(len(nums)):
            if i > 0:
                left += nums[i - 1]

            right = sums - left - nums[i]

            if left == right:
                return i

        return -1


solution = Solution()
print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))