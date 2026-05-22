class Solution:
    
    def longestKSubstr(self, s, k):
        
        low = 0
        high = 0
        
        hashmap = {}
        res = -1
        
        while high < len(s):
            
            # add current character
            hashmap[s[high]] = hashmap.get(s[high], 0) + 1
            
            # shrink window if unique chars > k
            while len(hashmap) > k:
                
                hashmap[s[low]] -= 1
                
                if hashmap[s[low]] == 0:
                    del hashmap[s[low]]
                
                low += 1
            
            # valid window
            if len(hashmap) == k:
                res = max(res, high - low + 1)
            
            high += 1
        
        return res
sol = Solution()
s = "aabacbebebe"   
k = 3
print(sol.longestKSubstr(s, k))
