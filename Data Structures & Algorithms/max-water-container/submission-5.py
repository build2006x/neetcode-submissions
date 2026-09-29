class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ### my understanding of the problem  ---> 
        ### what is the compute we need to do
        """
        take the indices and minus them and take the both values and do the 
        compute push to a array or maintain the max container water 
        """

        max_val = 0 

        l = 0
        r = len(heights) - 1

        while l < r:
                width  = r - l 
                tall = min(heights[l],heights[r])
                max_val = max(max_val,width*tall)
                if width*tall > max_val:
                        max_val = width*tall
                if heights[l]  < heights[r]:
                        l +=1
                else:
                        r -=1

                width = 0
                tall = 0
                
        return max_val

                  
 

 

