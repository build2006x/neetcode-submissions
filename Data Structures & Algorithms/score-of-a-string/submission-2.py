class Solution:
    def scoreOfString(self, s: str) -> int:
            
            left = 0
            right = 1
            sum_val  = 0
            result = 0

            while right < len(s):
                          sum_val  = abs(ord(s[left]) - ord(s[right]))
                          result += sum_val
                          sum_val = 0
                          right +=1
                          left +=1
            
            return result 

          