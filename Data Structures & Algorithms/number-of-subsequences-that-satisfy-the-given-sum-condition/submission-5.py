class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        count = 0
        l = 0
        r = len(nums) -1 
        n = sorted(nums)

        while l <= r:
                if n[l] + n[r] <= target:
                        n_val = r - l 
                        val = pow(2,n_val)
                        count += val
                        l +=1
                elif n[l] + n[r] < target:
                       l +=1
                else:
                     r -=1

        ans =  count % (10**9 + 7)
        return ans  