1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        def reverser(start,end):
4            while start<end:
5                nums[start],nums[end]=nums[end],nums[start]
6                start+=1
7                end-=1
8        n=len(nums)
9        k=k%n
10        reverser(0,n-1)
11        reverser(0,k-1)
12        reverser(k,n-1)
13
14        """
15        Do not return anything, modify nums in-place instead.
16        """
17        