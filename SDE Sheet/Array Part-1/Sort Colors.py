    def sortColors(self, nums: List[int]) -> None:
        for i in range(2,-1,-1):
            for j in range(len(nums)):
                if nums[j]==i:
                    nums.insert(0,nums[j])
                    nums.pop(j+1)
