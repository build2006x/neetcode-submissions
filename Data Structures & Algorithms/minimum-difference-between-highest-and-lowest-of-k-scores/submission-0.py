class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = sorted(nums)
        l = 1
        r = k 
        min_val =  n[k-1] - n[0]
        while r < len(nums):
              new = n[r]-n[l]
              min_val = min(min_val,new)
              l +=1
              r +=1
        
        return min_val