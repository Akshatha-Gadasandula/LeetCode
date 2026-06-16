class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            diff= target - nums[i]
            if diff in dict1:
                return [i,dict1[diff]]
            else:
                dict1[nums[i]] = i
        
