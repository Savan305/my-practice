class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Track maximum frequency character
            max_freq = max(max_freq, freq[s[right]])

            # If replacements needed > k, shrink window
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
sol = Solution()
print(sol.characterReplacement("AABABBA", 1))   
