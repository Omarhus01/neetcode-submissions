class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        group = defaultdict(list) #{key , the characters : the value will be the list of these words }


        for s in strs: 
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] +=1 #I was so fucking stupid and I missed the = here this si why there was not count at all
            print(count)
            
            group[tuple(count)].append(s)
        return list(group.values())

