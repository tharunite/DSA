1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        stack=[]
4        for directory in path.split('/'):
5            if directory=='' or directory=='.':
6                continue
7            elif directory=='..':
8                if stack:
9                    stack.pop()
10                else:
11                    continue
12            else:
13                stack.append(directory)
14        return '/'+'/'.join(stack)
15