class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        sum_val = 0 

        pointer = 0

        while pointer < len(customers): 
                if grumpy[pointer] == 0:
                      sum_val += customers[pointer]
                pointer +=1
        
        window_sum = 0
        
        for i in range(0,minutes):
                if grumpy[i] == 1:
                        window_sum +=customers[i]
        
        l = 0
        r = minutes
        new = window_sum

        while r < len(customers):
                if grumpy[r] == 1:
                            new += customers[r]
                if grumpy[l] == 1:
                            new -=customers[l]
                window_sum = max(window_sum,new)
                l +=1
                r +=1
        

        return sum_val +  window_sum
                    
