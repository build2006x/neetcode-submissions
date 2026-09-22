class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ### the logic i am thining using the two pointer
        ### keep a two pointer l and r 
        ### if the once l and r equal and move r once the r more than two 
        ### set a variable ping to last r 
        ## came out of the loop and del the el in the array 

        pointer = 0
        vaild = 0
        count = 0
        reader = 0 
        res = []
        k = 0

        for i in nums:
            if i not in res:
                res.append(i)

        while pointer < len(res):
                while reader < len(nums):
                    if res[pointer] == nums[reader]:
                            count +=1
                            nums[vaild] = nums[reader]
                            vaild +=1
                            if count == 2:
                                    break
                    reader +=1
                reader  = 0
                count = 0
                pointer +=1
        
        return vaild 

                            

                        
        
                     
                                
                    




            
                    



                         
            
                 




