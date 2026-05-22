class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high = 0
        res = 0
        last_index = {}

        while high < len(s):

            # if character already exists in current window
            if s[high] in last_index and last_index[s[high]] >= low:
                low = last_index[s[high]] + 1

            # update latest index
            last_index[s[high]] = high

            # update result
            res = max(res, high - low + 1)

            # move high pointer
            high += 1

        return res
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
