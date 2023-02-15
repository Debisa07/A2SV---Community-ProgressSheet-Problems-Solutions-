// https://leetcode.com/problems/minimum-increment-to-make-array-unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        count = 0

        for i in range(1,n):

            if nums[i] <= nums[i-1]:
                diff = nums[i-1] + 1 - nums[i]
                count += diff
                nums[i] = nums[i-1] + 1
                
        return count