class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        reader  = 0
        pointer = 0
        set_val = set()
        k = 0

        while pointer < len(nums):
                if nums[pointer] not in set_val:
                    nums[reader] = nums[pointer]
                    set_val.add(nums[reader])
                    reader +=1
                    k +=1
                pointer +=1
        
        return k


                   
                    