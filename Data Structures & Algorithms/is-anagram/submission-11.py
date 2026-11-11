class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        res =  [0] *26
        for count_s in s:
            res[ord(count_s) - ord('a')] += 1 

        for count_t in t:
            res[ord(count_t) - ord('a')] -= 1
            if res[ord(count_t) - ord('a')] < 0:
                return False
        
       
        return True
        

