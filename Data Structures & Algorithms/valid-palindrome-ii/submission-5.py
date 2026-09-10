class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        ### as logic what we did is going to do now 


        aphabet = [chr(i) for i in range(97, 123)]
        numbers = [chr(i) for i in range(48, 58)]

        real_string = ""
        pointer  = 0 

        while pointer < len(s):
                if s[pointer].lower() in aphabet:
                       real_string += s[pointer].lower()
                pointer +=1
        
        read_pointer = 0 
        check_string = ""

     

        while read_pointer < len(real_string):
                check_string = real_string[:read_pointer] +  real_string[read_pointer+1:]
                print(check_string)
                if check_string == check_string[::-1]:
                          return True 
                read_pointer +=1
        
        return False





 