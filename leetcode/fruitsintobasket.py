class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        low = 0
        high = 0
        max_length = 0
        hashmap = {}
        while high < len(fruits):
            hashmap[fruits[high]] = hashmap.get(fruits[high],0)+1
            while len(hashmap)>2:
                if hashmap[fruits[high]] == hashmap[fruits[high+1]]:
                    break
                    
            max_length = max(max_length, high-low+1)
            high += 1
        return max_length
sol = Solution()
print(sol.totalFruit([1,2,1]))
        
                    