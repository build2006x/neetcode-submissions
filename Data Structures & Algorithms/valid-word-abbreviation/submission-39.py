class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

          one_pointer = 0
          two_pointer = 0

          while one_pointer < len(word) and two_pointer < len(abbr):
                    if word[one_pointer] == abbr[two_pointer]:
                         one_pointer +=1
                         two_pointer +=1

                    elif abbr[two_pointer].isalpha() or abbr[two_pointer] == '0':
                         return False
                    else:
                         sub = 0
                         while  two_pointer < len(abbr) and abbr[two_pointer].isdigit():
                                   sub = sub *  10 + int(abbr[two_pointer]) 
                                   two_pointer +=1
                         one_pointer += sub  
          
          return one_pointer == len(word) and two_pointer == len(abbr)
          
     
  
 






