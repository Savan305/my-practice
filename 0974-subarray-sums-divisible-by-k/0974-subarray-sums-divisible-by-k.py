class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}      # remainder -> frequency
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            remainder = prefix % k

            if remainder in count:
                ans += count[remainder]

            count[remainder] = count.get(remainder, 0) + 1

        return ans