class Solution:
    def countTriplets(self, target, arr):
        arr.sort()
        ans = 0
        i=0
        left = i+1
        right = len(arr)-1
        while left<right:
            c_sum = arr[i]+arr[left]+arr[right]

            if c_sum>= target:
                right-=1
            else:
                ans = ans + (right-left)
                left+=1
        return ans
sol = Solution()
print(sol.countTriplets(2,[-2,0,1,3]))
                