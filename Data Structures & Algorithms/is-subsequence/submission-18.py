class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
             
            scount = 0
            tcount = 0 

            if len(s) == 0:
                        return True

            while tcount < len(t):
                            if s[scount] == t[tcount]:
                                            scount +=1
                            if scount == len(s):
                                            return True
                            tcount +=1
                            
            return False
