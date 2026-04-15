class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen  = set()
        n = len(nums) // 2

        for i in range(n + 2):
            if nums[i] not in seen:
                seen.add(nums[i])
            else: return nums[i]

        
