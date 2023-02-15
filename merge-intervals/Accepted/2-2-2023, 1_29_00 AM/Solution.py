// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals):
        result = []
        intervals.sort()
        for interval in intervals:
            if len(result)==0 or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])
            
        return result