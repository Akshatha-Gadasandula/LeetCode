class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) -1
        for i in range(len(nums)):
            if nums[i] == target:
                return i

            elif nums[r]== target:
                return r
            else:
                r = r-1
        return -1   
