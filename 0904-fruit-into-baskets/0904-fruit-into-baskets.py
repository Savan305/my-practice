class Solution:
    
    def totalFruit(self, fruits: list[int]) -> int:
        
        low = 0
        high = 0
        
        hashmap = {}
        max_length = 0
        
        while high < len(fruits):
            
            # add current fruit
            hashmap[fruits[high]] = hashmap.get(fruits[high], 0) + 1
            
            
            # shrink window if more than 2 fruit types
            while len(hashmap) > 2:
                
                hashmap[fruits[low]] -= 1
                
                # remove fruit from hashmap if count becomes 0
                if hashmap[fruits[low]] == 0:
                    del hashmap[fruits[low]]
                
                low += 1
            
            
            # update answer
            max_length = max(max_length, high - low + 1)
            
            high += 1
        
        return max_length


        