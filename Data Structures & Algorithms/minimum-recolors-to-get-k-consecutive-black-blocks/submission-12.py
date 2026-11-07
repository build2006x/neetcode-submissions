class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = k
        c_count = Counter(blocks[0:k])
        min_colour = c_count['W']
        re = []
        re.append(min_colour)

        while r < len(blocks):
                if blocks[r] == 'W':
                        min_colour +=1
                if blocks[l] == 'W':
                       min_colour -=1
                re.append(min_colour)  
                r +=1
                l +=1      
        
        return min(re)