class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        first = 0 
        second =  first + 1
        last = -1
        last_before = -2 

        nums_sorted = sorted(nums)

        ans = (nums_sorted[last] * nums_sorted[last_before]) - (nums_sorted[first] * nums_sorted[second])

        return ans

                