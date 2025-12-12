1class Solution:
2    def isValid(self, s: str) -> bool:
3        brackets={'{':'}','[':']','(':')'}
4        stack=[]
5        for letter in s:
6            if letter in brackets:
7                stack.append(letter)
8            elif letter in brackets.values():
9                if not stack or brackets[stack[-1]]!=letter:
10                    return False
11                stack.pop()
12            else: pass
13        return len(stack)==0
14            
15