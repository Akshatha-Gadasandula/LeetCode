class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0 
        max_sum= float('-inf')
        for i in range(len(nums)):
            sum = sum + nums[i]
            sum = max(sum,nums[i])
            max_sum = max(sum,max_sum)
        return max_sum


        
