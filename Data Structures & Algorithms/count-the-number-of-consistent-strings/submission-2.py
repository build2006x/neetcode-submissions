class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        reader = 0
        base_pointer = 0
        flag = 0
        result = 0

        while base_pointer < len(words):
                for i in words[base_pointer]:
                        if i in allowed:
                            continue
                        else:
                             flag  = 1
                if flag == 0:
                    result +=1
                base_pointer +=1
                flag  = 0
        
        return result
                