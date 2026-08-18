class Solution:
    def findLucky(self, arr: List[int]) -> int:

        result = 0
        ar = Counter(arr)

        for fre,val in ar.items():
            if fre == val:
                result = max(result,val)

        if result == 0:
            return -1
        else:
            return result
        