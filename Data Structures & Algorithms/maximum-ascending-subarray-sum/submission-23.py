class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
                left = 0
                right = 1
                start = 0
                max_sum = 0

                while right < len(nums):
                                if nums[left] < nums[right]:
                                                right +=1
                                                left +=1
                                                max_sum = max(max_sum,sum(nums[start:right]))
                                else:
                                                max_sum = max(max_sum ,sum(nums[start:right]))
                                                start = right
                                                end = start 
                                                left +=1
                                                right +=1

                return max_sum
                
                                                
              
            