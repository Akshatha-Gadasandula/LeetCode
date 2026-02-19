#Permutations 2
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        def backtracking2(path):
            if len(path)==len(nums) and path not in res:
                res.append(path[:])
            for i in range(len(nums)):
                if used[i]:continue
                used[i]=True
                path.append(nums[i])
                backtracking2(path)
                path.pop()
                used[i]=False
            return res
        return backtracking2([])
