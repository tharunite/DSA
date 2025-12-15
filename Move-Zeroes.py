1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        last_nonzero=0
4        for i in range(len(nums)):
5            if nums[i]!=0:
6                nums[last_nonzero],nums[i]=nums[i],nums[last_nonzero]
7                last_nonzero+=1
8
9
10        