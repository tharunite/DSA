1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if not nums:
4            return None
5        if len(nums)==1:
6            return nums[0]
7        slow=0
8        for fast in range(1,len(nums)):
9            if nums[slow]!=nums[fast]:
10                slow+=1
11                nums[slow]=nums[fast]
12        return slow+1