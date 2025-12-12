def mergesort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left=mergesort(nums[:mid])
    right=mergesort(nums[mid:])
    merged=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

