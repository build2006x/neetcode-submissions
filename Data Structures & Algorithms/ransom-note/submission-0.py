class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag_count = Counter(magazine)
        ran_count = Counter(ransomNote)

        for key,val in ran_count.items():
            if ran_count[key] <= mag_count[key]:
                pass
            else:
                 return False
        
        return True

        