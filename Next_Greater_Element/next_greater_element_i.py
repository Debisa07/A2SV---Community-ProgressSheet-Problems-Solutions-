class Solution(object):
    def nextGreaterElement(self, findNums, nums):
      
        cache, st = {}, []
        for x in nums:
            while len(st) > 0 and st[-1] < x:
                cache[st.pop()] = x
            st.append(x)
        result = [-1 for e in findNums ]
        for idx,x in enumerate(findNums):
            if x in cache:
                result[idx] = cache[x]
        return result