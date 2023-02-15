// https://leetcode.com/problems/add-strings

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        tem='%d' %eval(num1+'+'+num2)
        return tem