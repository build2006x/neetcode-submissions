class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

        p1 = 0
        p2 =  1
        T = 1

        if rowIndex <= len(result)-1:
             return result[rowIndex]
        else:
            while len(result)-1 != rowIndex:
                new = []
                new.append(1)
                while p2 < len(result[-1]):
                    add = result[-1][p1] + result[-1][p2]
                    new.append(add)
                    p2 +=1
                    p1 +=1
                new.append(1)
                p1 = 0
                p2 = p1 + 1
                result.append(new)
                T -=1
        
        return result[-1]



                