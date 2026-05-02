class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1 = [0] * 26 
        count_2 = [0] * 26 

        for c1 in s:
            count_1[ord(c1)- ord('a')] += 1
        
        for c2 in t:
            count_2[ord(c2)- ord('a')] += 1
        
        return count_1 == count_2
