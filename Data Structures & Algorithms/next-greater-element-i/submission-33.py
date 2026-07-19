class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
                                pointer = 0
                                reader  = 0
                                result =  []

                                while pointer < len(nums1):
                                                for idx,val  in enumerate(nums2):
                                                            if nums1[pointer] == nums2[idx]:
                                                                            for i in range(idx+1,len(nums2)):
                                                                                                    if  nums2[i] > nums1[pointer]:
                                                                                                                    result.append(nums2[i])
                                                                                                                    break
                                                                                                    elif i == len(nums2)-1:
                                                                                                                        result.append(-1)
                                                                                                                        break
                                                                            if idx == len(nums2)-1: 
                                                                                            result.append(-1)                           
                                                pointer +=1  

                                return result                      
                                  