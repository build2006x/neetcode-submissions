class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

      arr = sorted(nums)
      pointer = 0
      result = []
      l = pointer + 1 
      r = len(arr) - 1

      while pointer < len(arr)-2:
              if pointer > 0 and arr[pointer] == arr[pointer-1]:
                      pointer +=1
                      continue 
              l = pointer + 1
              r = len(arr) - 1
              while l < r:
                      if arr[pointer]+arr[l]+arr[r] == 0:
                              result.append([arr[pointer],arr[l],arr[r]])
                              while l < r and arr[l] == arr[l+1]:
                                      l +=1
                              while l < r and arr[r] == arr[r-1]:
                                      r -=1
                              l +=1
                              r -=1
                      elif arr[l]+arr[r] < abs(arr[pointer]):
                              l +=1
                      else:
                              r -=1
              pointer +=1
              
      
      return result