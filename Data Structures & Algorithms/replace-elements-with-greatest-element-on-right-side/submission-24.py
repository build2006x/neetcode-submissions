class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
             

            fix = 0
            read  = 1

            greater  = float('-inf')

            while fix < len(arr):
                            while read < len(arr): 
                                        greater = max(greater,arr[read])
                                        read +=1
                            if fix == len(arr)- 1:
                                    arr.pop()
                                    break
                            arr[fix] = greater 
                            fix +=1
                            read = fix + 1
                            greater  = 0
            arr.append(-1)
            return arr

                        