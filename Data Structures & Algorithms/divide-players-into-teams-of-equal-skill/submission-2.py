class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l = 1
        r = len(skill) -2 
        n = sorted(skill)

        sum_val = n[0]+n[-1]
        res = n[0]*n[-1]

        while l < r: 
                if n[l]+n[r] == sum_val:
                        res += n[l] * n[r]
                        l +=1
                        r -=1
                else:
                    return -1

        return res    
