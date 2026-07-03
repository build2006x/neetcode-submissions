class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            count = Counter(nums)
            max_val = 0

            for i in count.values():
                         max_val = max(max_val,i)
                         
            for i,j in count.items():
                        if j == max_val:
                                   return i
            
