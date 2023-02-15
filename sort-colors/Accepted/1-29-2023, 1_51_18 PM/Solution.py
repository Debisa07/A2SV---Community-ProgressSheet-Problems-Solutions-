// https://leetcode.com/problems/sort-colors

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
  
        num = 0
        for _ in range(len(nums)):
            if nums[num] == 0:
                nums.pop(num)
                nums.insert(0, 0)
                num += 1
            elif nums[num] == 2:
                nums.pop(num)
                nums.append(2)
            else:
                num += 1
        return