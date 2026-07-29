class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
            ###  what i am thinking is can you make
            ###  a array to store the number based on the  

            result = []
            store  = []
     
            for i in range(1,len(nums)+1):
                          store.append(i)
            print(store)
            for j in store:
                     if j not in nums and j!=nums[0]:
                           result.append(j)
            
            return result
