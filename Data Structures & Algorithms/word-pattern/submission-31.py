class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

                        arr = s.split(" ")

                        if len(pattern) != len(arr):
                                        return False
                        result = {}
                        checker = set() 

                        for idx,i in enumerate(pattern):
                                        if i  in  result:
                                                if result[i] != arr[idx]:
                                                                return False
                                        else:
                                                  if arr[idx] in checker:
                                                                return False
                                                  result[i] = arr[idx]
                                                  checker.add(arr[idx])  
                                                    
                                          
                        
                        return True

                                                        
        