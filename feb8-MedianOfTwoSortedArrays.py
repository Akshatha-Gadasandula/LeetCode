#Median of two sorted arrays
#problem number - 4
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # First merge two arrays

        merged = nums1+nums2
        merged.sort()
        left = 0
        right = len(merged)-1
        if len(merged)%2 == 1:
            return merged[int(right/2)]
        else:
            mid = len(merged)//2
            return (merged[mid]+merged[mid-1])/2
