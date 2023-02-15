// https://leetcode.com/problems/assign-cookies

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        glen = len(g)
        j=0
        count=0
        for i in xrange(len(s)):
            if s[i]>=g[j]:
                count+=1
                if j==glen-1:
                    break
                j+=1
        return count