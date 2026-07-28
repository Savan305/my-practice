class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0

        hashmap = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in hashmap:
                length = i - hashmap[count]
                max_length = max(max_length, length)
            else:
                hashmap[count] = i

        return max_length