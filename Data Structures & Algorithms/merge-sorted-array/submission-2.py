class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        reader = 0
        num2_pointer = 0

        while reader < len(nums1):
              if nums1[reader] == 0 and num2_pointer < len(nums2):
                  nums1[reader],nums2[num2_pointer] = nums2[num2_pointer],nums1[reader]
                  num2_pointer +=1
              reader +=1
        
        l = 0 
        r = 1
        pointer = 0
        while pointer < len(nums1):
                while r < len(nums1):
                        if nums1[l] > nums1[r]:
                            nums1[l],nums1[r] = nums1[r],nums1[l]
                        l +=1
                        r +=1
                l = 0
                r = l + 1 
                pointer +=1
                
        return nums1
                
                  

             
                
        