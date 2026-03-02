class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []

        for i in range(len(nums) - k + 1):
            count = Counter(nums[i:i+k])
            if len(count) <= x:
                ans.append(sum(nums[i:i+k]))
            else:
                pairs = list(count.items())
                pairs.sort(key = lambda p: (p[1], p[0]), reverse=True)
                currSum = 0
                for num, freq in pairs[:x]:
                    currSum += (num*freq)
                ans.append(currSum)
        return ans
