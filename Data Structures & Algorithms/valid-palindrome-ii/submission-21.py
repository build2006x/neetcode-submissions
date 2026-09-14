class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        chars = list(s)

        if chars == chars[::-1]:
            return True

        for i in range(len(chars)):
            removed = chars.pop(i)          # remove char at i
            if chars == chars[::-1]:        # check palindrome
                return True
            chars.insert(i, removed)        # add back the char

        return False


             