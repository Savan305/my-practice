class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0

        # HashMap: prefix_sum -> frequency
        prefix_map = {0: 1}

        for num in nums:
            # Calculate current prefix sum
            prefix_sum += num

            # Check if required previous prefix sum exists
            needed = prefix_sum - k

            if needed in prefix_map:
                count += prefix_map[needed]

            # Store current prefix sum
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] += 1
            else:
                prefix_map[prefix_sum] = 1

        return count