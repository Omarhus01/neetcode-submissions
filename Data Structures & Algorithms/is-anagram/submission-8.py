class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}


        for c in s:
            if c in first:
                first[c] += 1
            else:
                first[c] = 1
        
        for ch in t:
            if ch in second:
                second[ch] += 1
            else:
                second[ch] = 1

        return first == second
         
       