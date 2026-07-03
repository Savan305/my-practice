class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        len(nums)//2
        first = nums[:n]
        second = nums[n:]
        for i in range(n):
            res.append(first[i])
            res.append(second[i])
        return res