// https://leetcode.com/problems/next-greater-node-in-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = []
        count = 0
        while head:
            res.append(0)
            while stack and stack[-1][1]<head.val:
                res[stack[-1][0]]=head.val
                stack.pop()
            stack.append([count,head.val])
            count+=1
            head = head.next
        return res