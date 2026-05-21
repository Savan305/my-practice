class Solution:
    def maxSubarraySum(self, arr, k):
        low = 0
        high = 1
        max_sum = 0
        c_sum = 0
        for i in range(low,high+1):
            c_sum+=arr[i]
            max_sum = max(max_sum,c_sum)
        
        while high<len(arr)-1:
            c_sum-=arr[low]
            low+=1
            high+=1
            c_sum+=arr[high]
            if c_sum>max_sum:
                max_sum = c_sum
        return max_sum

arr = [100, 200, 300, 400]
k = 2

obj = Solution()
print(obj.maxSubarraySum(arr, k))
                

        