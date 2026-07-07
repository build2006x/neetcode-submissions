class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                pointer  = 0 
                move_pointer = 0
                result  = []

                while pointer < len(strs):
                            result.append([strs[pointer]])
                            while move_pointer < len(strs):
                                        if move_pointer != pointer:
                                                   if sorted(strs[move_pointer]) == sorted(strs[pointer]):
                                                                result[pointer].append(strs[move_pointer])
                                        move_pointer +=1
                            move_pointer = 0
                            pointer +=1

                new_result = []

                for i in result:
                        new = sorted(i)
                        if new not in new_result:
                                      new_result.append(new)    
                        new  = []        
                 
                return new_result 
                        