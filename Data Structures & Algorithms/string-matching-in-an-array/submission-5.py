class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
                move_pointer = 0
                pointer = 0
                result = []
                while pointer < len(words):
                            while move_pointer < len(words):
                                        if words[pointer] != words[move_pointer] and words[pointer] in words[move_pointer]:
                                                result.append(words[pointer]) 
                                        move_pointer +=1
                            pointer +=1
                            move_pointer  = 0

                new = []

                for i in result:
                             if i not in  new:
                                    new.append(i)
                return new
                                                                               
         