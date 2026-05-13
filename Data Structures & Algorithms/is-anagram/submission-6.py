class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s1 = {}
        t1 = {}

    
        for c in s:
            if c not in s1:
                s1[c]  = 0
            s1[c] +=1
        
        for ch in t:
            if ch  not in t1:
                t1[ch] = 0
            t1[ch] +=1

        return s1 == t1
       