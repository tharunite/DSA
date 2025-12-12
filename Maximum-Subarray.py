1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        suma = nums[0]
4        max_suma = nums[0]
5        
6        for i in range(1, len(nums)):
7            if suma < 0:
8                suma = nums[i]    
9            else:
10                suma += nums[i]
11            if suma > max_suma:
12                max_suma = suma
13                
14        return max_suma
15