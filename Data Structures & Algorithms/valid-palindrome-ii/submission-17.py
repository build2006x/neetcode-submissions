class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        pointer = 0
        s_string =  ""

        if s[::-1] == s:
            return True

        while pointer < len(s):
              s_string = s[:pointer] + s[pointer+1:]
              if s_string == s_string[::-1]:
                 return True
              pointer +=1
              s_string = ""
        
        return False 


             