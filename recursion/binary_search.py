def binaryS(arr,ele):
    high=len(arr)-1
    low=0
    mid=(high+low)//2
    if arr[mid]==ele:
        return mid
    elif ele>arr[mid]:
        binaryS(arr[mid+1:],ele)
    elif ele<arr[mid]:
        binaryS(arr[:mid],ele)
    return -1
        