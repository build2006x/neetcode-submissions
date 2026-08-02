class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

                            pointer = 0
                            reader = 0

                            store = []
                            arr = []
                            miss = 0
                            repeat = 0

                            while pointer < len(grid):
                                            reader = 0
                                            while reader < len(grid[pointer]):
                                                        arr.append(grid[pointer][reader])
                                                        if grid[pointer][reader] in store:
                                                            repeat = grid[pointer][reader]
                                                        else:
                                                            store.append(grid[pointer][reader]) 
                                                        reader +=1
                                            pointer +=1
                            print(arr)
                            for i in range(1,len(arr)+1):
                                                if i not in arr:
                                                        miss= i
                                                        return [repeat,miss]
             