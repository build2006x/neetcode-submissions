class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
                string = ""
                result = []

                for i in range(0,len(arr)):
                            for j in range(0,len(arr)):
                                        if arr[i] == arr[j] and i != j:
                                            string = ""
                                            break
                                        else:
                                            string = arr[i] 
                            if string != "":
                                        result.append(string)
                                        string = ""

                try:
                         return result[k-1]
                except IndexError:
                          return ""
                
                
                

                        
                
