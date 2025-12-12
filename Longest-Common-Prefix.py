1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        if not strs: return ''
4        if len(strs)==1:return strs[0]
5
6        prefix=strs[0]
7        for word in strs[1:]:
8            while not word.startswith(prefix):
9                prefix=prefix[:-1]
10                if prefix=='':
11                    return ''
12        return prefix
13                
14
15        