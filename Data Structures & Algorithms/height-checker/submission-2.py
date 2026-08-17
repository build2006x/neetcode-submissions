class Solution:
    def heightChecker(self, heights: List[int]) -> int:
           
                    expected =  sorted(heights)
                    pointer = 0 
                    count = 0

                    while pointer < len(heights):
                                    if expected[pointer] != heights[pointer]:
                                                            count +=1
                                    pointer +=1

                    return count 
