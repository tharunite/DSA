1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        if not nums: return None
4        sums=[nums[0]]
5        for i in range(1,len(nums)):
6            sums.append(sums[-1]+nums[i])
7        return sums
8            
9        