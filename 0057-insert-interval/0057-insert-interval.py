from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Insert newInterval at the correct position
        inserted = False
        res1 = []

        for interval in intervals:
            if not inserted and interval[0] >= newInterval[0]:
                res1.append(newInterval)
                inserted = True
            res1.append(interval)

        if not inserted:
            res1.append(newInterval)

        # Merge intervals
        res = []
        start, end = res1[0]

        for i in range(1, len(res1)):
            s, e = res1[i]

            if end >= s:
                end = max(end, e)
            else:
                res.append([start, end])
                start, end = s, e

        res.append([start, end])

        return res