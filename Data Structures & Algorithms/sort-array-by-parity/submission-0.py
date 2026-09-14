class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        pointer = 0
        reader = 0

        while pointer < len(nums):
             if nums[pointer] % 2 == 0 :
                   nums[reader],nums[pointer] = nums[pointer],nums[reader]
                   reader +=1
             pointer +=1

        return nums 