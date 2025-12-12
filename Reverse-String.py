1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        if s is None or s==[]: return None
4        if len(s)==1: return s
5        start=0
6        end=len(s)-1
7
8        while start<end:
9            s[start],s[end]=s[end],s[start]
10            start+=1
11            end-=1