class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left<right:
                c_sum = nums[i]+nums[left]+nums[right]

                if abs(c_sum-target)<abs(closest-target):
                    closest = c_sum

                if c_sum <target :
                    left+=1
                elif c_sum > target:
                    right-=1
                else:
                    return c_sum
        return closest
    
sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4],1))


            
       