class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        lookup = {}
        for task in tasks:
            lookup[task] = lookup.get(task, 0) + 1
        max_freq = max(lookup.values())
        res = (max_freq-1) * (n+1)
        for freq in lookup.values():
            if freq == max_freq:
                res += 1
        return max(len(tasks), res)