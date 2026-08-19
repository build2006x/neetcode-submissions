class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

            left = 0
            right = 1
            flag = 0

            while right < len(nums):
                    if nums[left] % 2 !=0 and nums[right] % 2 == 0:
                        left +=1
                        right +=1
                    elif nums[left] % 2 ==0 and nums[right] % 2 != 0:
                        right +=1
                        left +=1
                    else:
                        flag = 1
                        break

            if flag == 0:
                return True
            else:
                return False

        