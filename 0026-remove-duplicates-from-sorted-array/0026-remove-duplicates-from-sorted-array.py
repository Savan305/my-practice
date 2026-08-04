class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        officer = 0
        res = 1
        cm = 1
        while cm<len(nums):
            if nums[cm] == nums[cm-1]:
                cm +=1
            else:
                nums[officer+1] = nums[cm]
                officer+=1
                res+=1
                cm+=1
        return res
nums = [1,1,1,2,2,3]
sol = Solution()
answer = sol.removeDuplicates(nums)
print(answer)
        