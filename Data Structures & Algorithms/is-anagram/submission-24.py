class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
             
            checker = 0

            if len(t) != len(s):
                          return False
        
            while checker != len(s):
                        for reader in range(0,len(t)):
                                          if s[checker] == t[reader]:
                                                      t = t[:reader] + t[reader+1:] 
                                                      break 
                        checker +=1
            
            if t == "":
                       return True
            else:
                   return False 

                                      
                                            
                                         

            