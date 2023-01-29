class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        
        for i, v in enumerate(citations):
            if v >= n - i: return n-i
            
        return 0