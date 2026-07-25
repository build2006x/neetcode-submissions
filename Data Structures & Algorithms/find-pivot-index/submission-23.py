class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
                    index =  len(nums) -1
                    result = 0


                    while index !=  0:
                                if sum(nums[:index]) == sum(nums[index+1:]):
                                        result = index
                                        index -=1     
                                else:
                                    index -=1

                
                    if result == 0 or result == 1 :
                                    if 0 == sum(nums[index+1:]):
                                                      return 0
                                    else:
                                                      return -1
                    else: 
                                  return result
