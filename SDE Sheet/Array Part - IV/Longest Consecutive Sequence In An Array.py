class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
# Convert to set for O(1) existence checks.
# List lookup (x in nums) is O(n), which would make the solution too slow.
        s = set(nums)
        longest = 0
# A number x is the start of a sequence only if x-1 is not present.
# This prevents recounting the same sequence multiple times.
        for x in s:

            if x - 1 not in s:

                length = 1
                curr = x

                while curr + 1 in s:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest
