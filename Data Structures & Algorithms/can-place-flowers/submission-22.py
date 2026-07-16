class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
                
                            new =  [0] + flowerbed  + [0]

                            pointer = 1

                            while pointer < len(new) - 1:
                                        if new[pointer-1] ==0 and new[pointer+1] == 0 and new[pointer]  ==0:
                                                                new[pointer] = 1
                                                                n -=1
                                        pointer +=1
                    
                            return n <= 0

