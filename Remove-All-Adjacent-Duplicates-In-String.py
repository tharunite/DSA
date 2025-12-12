1class Solution:
2    def removeDuplicates(self, s: str) -> str:
3        stack = []
4        for ch in s:
5            if stack and stack[-1] == ch:
6                stack.pop()
7            else:
8                stack.append(ch)
9        return ''.join(stack)
10