// https://leetcode.com/problems/power-of-three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 3 or n == 1:
            return True
        else:
            n =n/3
            return self.isPowerOfThree(n)
        return False