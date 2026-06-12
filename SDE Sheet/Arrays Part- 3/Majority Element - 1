class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums)):
            if nums[i] not in s:
                count = 0
                s.add(nums[i])
                for j in range(len(nums)):
                    if nums[j] == nums[i]:
                        count = count +1
                if count > len(nums)//2:
                    return nums[i]

            
            

        
