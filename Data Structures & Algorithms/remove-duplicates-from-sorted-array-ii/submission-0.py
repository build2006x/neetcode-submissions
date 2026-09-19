class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #### question understanding 
        ### if more number are more than two remove rest the number 
        ### after remvoing still the order should be follow 
                
        ### brute fore logic 

        read_counter = 0
        k = len(nums) 
        s = []
        pointer = 0

        for i in nums:
            if i in s:
                pass
            else:
                s.append(i)

        while pointer < len(s):
            read_counter = 0
            for i in range(len(nums)-1,-1,-1):
                    if nums[i] == s[pointer]:
                            read_counter +=1
                            if read_counter > 2:
                                    nums.pop(i)
                                    k -=1
            pointer +=1

        return k           
                    



                         
            
                 




