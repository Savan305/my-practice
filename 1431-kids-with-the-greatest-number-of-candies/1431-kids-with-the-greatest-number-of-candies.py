# class Solution:
#     def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
#         return [c + extraCandies >= max(candies) for c in candies]
        
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= max_candies)

        return result