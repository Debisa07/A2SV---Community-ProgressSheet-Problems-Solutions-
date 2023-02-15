// https://leetcode.com/problems/pancake-sorting

class Solution:
  def pancakeSort(self, l: List[int]) -> List[int]:
    ans = []

    for target in range(len(l), 0, -1):
      index = l.index(target)
      l[:index + 1] = l[:index + 1][::-1]
      l[:target] = l[:target][::-1]
      ans.append(index + 1)
      ans.append(target)

    return ans