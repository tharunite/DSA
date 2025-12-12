1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        low=0
4        high=0
5        max_profit=0
6        for i in range(len(prices)):
7            if prices[i]<prices[low]:
8                low=i
9                continue
10            if prices[i]-prices[low]>max_profit:
11                max_profit=prices[i]-prices[low]
12        return max_profit
13            
14
15        
16        