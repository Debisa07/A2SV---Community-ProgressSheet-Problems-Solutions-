class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result, stack = [0] * len(temperatures), []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                pre_idx = stack.pop()
                result[pre_idx] = i - pre_idx
            stack.append(i)
        return result
