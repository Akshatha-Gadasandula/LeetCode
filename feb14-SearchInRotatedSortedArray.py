#Search In Rotated Sorted Array
#Problem Number - 33
class Solution:
    def search(self, nums, target: int) -> int:
        def find(start,end):
            if end<=start:
                return -1 if nums[end]!= target else end
            mid=start+(end-start)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[start]:
                if nums[mid]<target and target<nums[start]:
                    return find(mid+1,end)
                return find(start,mid-1)
            if nums[end]<nums[start]:
                if target>nums[start] and target<nums[mid]:
                    return find(start,mid-1)
                if target==nums[start]:
                    return start
                return find(mid+1,end)
            else:
                if nums[mid]>target:
                    return find(start,mid-1)
                    
                return find(mid+1,end)
        return find(0,len(nums)-1)
