class Solution(object):
    def numIdenticalPairs(self, nums):
        output = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    output += 1
        return output