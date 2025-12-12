1class Solution:
2    def subarraySum(self, nums: list[int], k: int) -> int:
3        running = 0
4        count_map = {0: 1}  # prefix sum 0 has occurred once
5        subs = 0
6        
7        for num in nums:
8            running += num
9            if running - k in count_map:
10                subs += count_map[running - k] 
11            count_map[running] = count_map.get(running, 0) + 1
12        
13        return subs
14