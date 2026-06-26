class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            
            nums_new = Counter(nums)

            for i in nums_new.values():
                            print(i)
                            if i > 1:
                                return True
            return False
            

                
