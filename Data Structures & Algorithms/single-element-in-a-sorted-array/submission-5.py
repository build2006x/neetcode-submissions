class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if len(nums) == 1:
             return nums[0]

        l = 0
        r = 1

        while r < len(nums):
                if  nums[l] == nums[r]:
                            l +=2
                            r +=2
                else:
                     return nums[l]
                     
        return nums[-1]

                        