class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ### here i we need to check weather the given array is increasing or decreasing

        p1 = 0
        p2 = 1

        while p2 < len(nums):
                if nums[p1] <= nums[p2]:
                      p1 +=1
                      p2 +=1
                      if p2 == len(nums):
                          return True
                else:
                      break

        p1 = 0
        p2 = 1

        while p2 < len(nums):
                if nums[p1] >= nums[p2]:
                      p1 +=1
                      p2 +=1
                      if p2 == len(nums):
                          return True
                else:
                     break
        
        return False
                
             