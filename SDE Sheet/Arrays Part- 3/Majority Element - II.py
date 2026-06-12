class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s = set()
        output = []
        dic = dict()
        for i in range(len(nums)):
            count = 0
            if nums[i] not in s:
                s.add(nums[i])
                dic[nums[i]] = 1
            elif nums[i] in s:
                dic[nums[i]] = dic[nums[i]] + 1
        for key,val in dic.items():
            if val > len(nums)//3:
                output.append(key)
        return output
