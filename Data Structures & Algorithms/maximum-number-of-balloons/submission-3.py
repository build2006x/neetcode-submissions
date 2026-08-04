class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
                    count  = 0
                    result = 0
                    substring = "balloon"

                    while True:
                                for i in substring:
                                        for idx,j in enumerate(text):
                                                if i == j:
                                                        text = text[0:idx] + text[idx+1:]
                                                        count +=1
                                                        break
                                if count == len(substring):
                                        count = 0
                                        result +=1
                                else:
                                        break
                    
                    return result 
