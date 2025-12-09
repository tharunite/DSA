1/**
2 * @param {number[]} nums
3 * @param {number} k
4 * @return {boolean}
5 */
6var containsNearbyDuplicate = function(nums, k) {
7    let window= new Set()
8    for(let i=0;i<nums.length;i++){
9        if(window.has(nums[i])){
10            return true
11        }
12        window.add(nums[i])
13        if(window.size>k){
14            window.delete(nums[i-k])
15        }
16    }
17    return false
18};