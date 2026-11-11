class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1= {}
        dic2 = {}

        for c1 in s:
            if c1 not in dic1:
                dic1[c1] = 0
            dic1[c1] +=1

        for c2 in t:
            if c2 not in dic2:
                dic2[c2] = 0
            dic2[c2] +=1
        
        return dic1 == dic2
        

       