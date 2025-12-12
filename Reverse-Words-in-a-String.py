1class Solution:
2    def reverseWords(self, s: str) -> str:
3        if s.strip() == "":
4            return ''
5        words = s.split()     
6        words = words[::-1]   
7        return ' '.join(words) 
8