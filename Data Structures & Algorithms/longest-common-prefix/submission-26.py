class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
             
            len_smallest = min(strs,key=len)
    
            prefix = ""
            
            for i in range(0,len(len_smallest)):
                        char = strs[0][i]
                        for words in strs:
                                if words[i] != char:
                                                return prefix 
                        prefix +=char
    
            return  prefix
            

                
                    
