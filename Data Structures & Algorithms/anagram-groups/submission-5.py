from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        #strs=["act","pots","tops","cat","stop","hat", "ACT", "POTS", "TOPS" , "CAT", "STOP", "HAT", "Abc", "bAc", "cab"]

        for s in strs:
            count = [0] * 52 
            for ch in s:
                if ch.islower():
                    count[ord(ch) - ord('a')] += 1
                else:
                    count[26 + ord(ch) - ord('A')] += 1
            
            groups[tuple(count)].append(s)

        print(groups)

        return list(groups.values())
                

        
