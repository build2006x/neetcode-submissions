class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = 0 
        count = 0
        r = k 

        while r <= len(arr):
                if sum(arr[l:r])//k >= threshold:
                    count +=1
                l +=1
                r +=1
        
        return count
            