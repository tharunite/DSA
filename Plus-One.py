1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        if digits[-1]!=9:
4            digits[-1]+=1
5            return digits
6        if len(digits)==1:
7            return [1,0]
8        digits[-1]=0
9        i=len(digits)-2
10        while i >=0:
11            if digits[i]!=9:
12                digits[i]+=1
13                return digits
14            digits[i]=0
15            i-=1
16        digits.insert(0,1)
17        return digits
18        