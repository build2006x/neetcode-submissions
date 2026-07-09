class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
                        real_len = len(nums)
                        pos = 0
                        pointer = 0 

                        while pointer < len(nums):
                                if nums[pointer] != val:
                                                nums[pos] = nums[pointer]
                                                pos +=1
                                pointer +=1
                        
                        for i in range(pos,len(nums)):
                                        nums[i] = 0
                                        real_len -=1

                        return real_len 
                
                 
                            