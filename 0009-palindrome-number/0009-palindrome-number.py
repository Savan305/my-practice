class Solution(object):
    def isPalindrome(self,s):
        s = str(s)
        if s==s[::-1]:
            return True
        else:
            return False
    
obj = Solution()
print(obj.isPalindrome(-121))
       
        