class Solution:
    def largestGoodInteger(self, num: str) -> str:


        static = 0
        dynamic = 1
        pointer = 0
        sol = []
        result = ""

        while pointer < len(num):
                if len(num[static:dynamic+1]) ==3 and num[dynamic] == num[dynamic-1]:
                              result = num[static:dynamic+1]
                              sol.append(result)
                              static = dynamic + 1
                              dynamic = static + 1

                elif dynamic < len(num) and num[static] == num[dynamic]:
                        dynamic +=1

                else:
                    static = dynamic 
                    dynamic = static + 1
                pointer +=1
        
        if len(sol) == 0:
               return ""
        else:
            return max(sol)