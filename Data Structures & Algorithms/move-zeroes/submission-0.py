class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ### simple logic i am thinking 

        ### keep a pointer --> to fill and query the the array if non zero 
        ### values if there fill the the the pointer poiting area 

        pointer = 0
        count = 0

        for i in nums:
             if i != 0:
                nums[pointer] = i
                pointer +=1
             else:
                count +=1
        
        while pointer < len(nums):
             nums[pointer] = 0
             pointer +=1

        return nums 