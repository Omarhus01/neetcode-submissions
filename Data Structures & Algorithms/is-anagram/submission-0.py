class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for char in s:
            if char not in dict_s:
                dict_s[char] = 1 
            dict_s[char] += 1
        
        for chars in t:
            if chars not in dict_t:
                dict_t[chars] = 1 
            dict_t[chars] += 1
        
        return dict_s == dict_t
