class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alphabet = [chr(i) for i in range(97, 123)]
        numbers = [chr(i) for i in range(48, 58)]
        main = ""
        pointer = len(s) - 1

        while pointer != -1:
                if s[pointer].lower() in alphabet:
                      main +=s[pointer].lower()

                elif s[pointer] in numbers:
                      main +=s[pointer]

                pointer -=1
        print(numbers)
        return main == main[::-1]   

