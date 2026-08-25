class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        main_pointer = 0
        p1 = 0
        p2 = 1
        count = 0 

        while main_pointer < len(nums):
                while p2 < len(nums):
                    if nums[p1] == nums[p2] and p1 < p2:
                         count +=1
                    p2 +=1
                p1 +=1
                p2 = p1 + 1
                main_pointer +=1

        return count