# class Solution:
#     def findSubarrays(self, nums: List[int]) -> bool:
#         for i in range(len(nums) - 3):
#             total = nums[i] + nums[i + 1]

#             if total == nums[i + 2] + nums[i + 3]:
#                 return True

#         return False
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            total = nums[i] + nums[i + 1]

            for j in range(i + 1, len(nums) - 1):
                if total == nums[j] + nums[j + 1]:
                    return True

        return False
