1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        if not strs: return ''
4        if len(strs)==1:return strs[0]
5
6        prefix=strs[0]
7        for word in strs[1:]:
8            for letter in range(min(len(word),len(prefix))):
9                if prefix[letter]!=word[letter]:
10                    prefix=prefix[:letter]
11                    break
12            prefix = prefix[:min(len(prefix), len(word))]
13        return prefix
14                
15
16        