class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
            
                    scount = 0
                    tcount = 0
                   
                    if len(t) == 0:
                            return 0

                    while scount < len(s):
                                    if tcount < len(t) and s[scount] == t[tcount]:
                                                tcount +=1
                                    scount +=1
                        
                    return len(t[tcount:])