class Solution:
  def reverseParentheses(self, s: str) -> str:
    stack = []
    ans = []

    for a in s:
      if a == '(':
        stack.append(len(ans))
      elif a == ')':
        b = stack.pop()
        ans[b:] = ans[b:][::-1]
      else:
        ans.append(a)
    return ''.join(ans)