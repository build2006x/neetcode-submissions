class Solution:
    def maxScore(self, s: str) -> int:
        
        ### the question is about we wanted 
        ### split the string and calculate the left 0 count and right 0 count 

                
        left = 0
        right = 1
        score = []
        mark = 0

        while left < len(s)-1:
                zero_count = Counter(s[:left+1])
                one_count = Counter(s[right:]) 
                mark = zero_count['0'] + one_count['1']
                score.append(mark)
                mark = 0
                left +=1
                right +=1
                zero_count = 0
                one_count = 0

        return max(score)