class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        we can have a default dictionary that we have it intialized with a list
        then we can have a count for each word , we count the occurrence 
        of each char in it and this should be our key 
        NOTE: we can't have3 it as a list since key is immutable so we need to pass it
        as a tuple . then we can append each word that has the 
        same key count 

        """
        res =  defaultdict(list) # now we know it will have empty list 

        # loop in each word and creat the emty alpha bet array
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord('a')] +=1  # this gets the ascii order of each char 
            res[tuple(count)].append(s)
        #print(type(res.values()))
        #print(res.values())
        return list(res.values())