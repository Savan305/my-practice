# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         left = 0
#         sums = sum(nums)

#         for i in range(len(nums)):
#             if i > 0:
#                 left += nums[i - 1]

#             right = sums - left - nums[i]

#             if left == right:
#                 return i

#         return -1

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * n
        suffix = [0] * n

        # Prefix sum
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        # Suffix sum
        suffix[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        # Compare left sum and right sum
        for i in range(n):
            left = 0 if i == 0 else prefix[i - 1]
            right = 0 if i == n - 1 else suffix[i + 1]

            if left == right:
                return i

        return -1


solution = Solution()
print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))
