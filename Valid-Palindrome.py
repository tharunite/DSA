1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s=s.strip().lower()
4        s=''.join(filter(str.isalnum,s))
5        for i in range(len(s)):
6            if s[i]!=s[-1-i]:
7                return False
8        return True
9        