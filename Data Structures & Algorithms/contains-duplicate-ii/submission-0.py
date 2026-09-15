class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        pointer= 0
        reader = 0

        while pointer < len(nums):
                while reader < len(nums) and reader != pointer:
                        if nums[reader] == nums[pointer] and abs(pointer-reader) <= k:
                                    return True
                        reader +=1
                pointer +=1
                reader = 0
        return False