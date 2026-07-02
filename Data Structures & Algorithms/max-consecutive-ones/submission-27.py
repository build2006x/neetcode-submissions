class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
                pointer = 0
                val = 0
                result = 0

                while pointer < len(nums):
                                if nums[pointer] == 1:
                                          val +=1
                                          result = max(result,val)
                                else:
                                       val = 0
                                pointer +=1
                return result
                                       
                                         

                         
