class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        plan:
        we need to store the frequency of all he chars, we are not caring about the order of them, so 
        we can use dictionary in this case, and from there we can compare both dictionaries immediately 
        if they are equalu, we return True immediately
        """

        d1 = {}
        d2= {}

        for ch in s:
            if ch not in d1:
                d1[ch] = 0
            d1[ch] += 1

        for char in t:
            if char not in d2:
                d2[char] = 0
            d2[char]+=1

        return d1 == d2
