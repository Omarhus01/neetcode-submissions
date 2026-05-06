class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for cs in s:
            if cs not in ds:
                ds[cs] =0 
            ds[cs]+=1
        
        for ct in t:
            if ct not in dt:
                dt[ct] =0 
            dt[ct]+=1
        return ds == dt 
