1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack=[]
4        for ele in tokens:
5            if ele=='+':
6                stack[-2]=stack[-2]+stack[-1]    
7                stack.pop()   
8            elif ele=='-':
9                stack[-2]=stack[-2]-stack[-1]
10                stack.pop()
11            elif ele=='/':
12                stack[-2]=int(stack[-2]/stack[-1])
13                stack.pop()
14            elif ele=='*':
15                stack[-2]=stack[-2]*stack[-1]
16                stack.pop()
17            else : stack.append(int(ele))
18        return stack[0]