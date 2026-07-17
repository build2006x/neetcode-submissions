class Solution:
    def maxDifference(self, s: str) -> int:
            
            odd = []
            even = []

            t = Counter(s)

            for i in  t.values():
                    if i %2  != 0:
                                 odd.append(i)
                    else:
                               even.append(i)

            pointer = 0
            max_diff  =  float('-inf')
            reader = 0

            while pointer < len(odd):
                    while reader < len(even):
                                 val = odd[pointer] - even[reader]
                                 max_diff = max(max_diff,val)
                                 reader +=1
                    reader = 0
                    pointer +=1
            
            return max_diff 
           