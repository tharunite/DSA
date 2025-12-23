1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        lastof1=m-1
4        lastof2=n-1
5        lastspot=len(nums1)-1
6        while lastof1>=0 and lastof2>=0:
7            if nums1[lastof1]>=nums2[lastof2]:
8                nums1[lastspot]=nums1[lastof1]
9                lastof1-=1
10                lastspot-=1
11            else:
12                nums1[lastspot]=nums2[lastof2]
13                lastof2-=1
14                lastspot-=1
15            
16        while lastof2 >= 0:
17            nums1[lastspot] = nums2[lastof2]
18            lastof2 -= 1
19            lastspot -= 1
20
21
22        
23       
24