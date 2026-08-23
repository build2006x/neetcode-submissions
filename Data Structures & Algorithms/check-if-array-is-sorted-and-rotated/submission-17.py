class Solution:
    def check(self, nums: List[int]) -> bool:
        pointer = 1


        if sorted(nums) == nums:
             return True

        while pointer < len(nums):
                rotated_arr = nums[pointer:] + nums[:pointer]
                if rotated_arr == sorted(nums):
                     return True
                pointer +=1
               
            
        return False 
