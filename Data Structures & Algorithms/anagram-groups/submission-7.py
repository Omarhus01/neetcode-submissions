from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        letter counts works as a key cause we need to look up the o equivalence of occurences of these
        chars in the fixed aplphabet list
        1) make a fixed array of the size of the alphabe, 
        2) use default dict  creates the list the frts time the key appears 
        3) we need to use built in functions ord, so we can get the place iof eahch char
        4) having a list of each char, to make it immutable, make t into a tuple
        5) we append each tuple in the default dice we created 
        then we return a loist of the lists of each tuple, we return the values only 
        '''
        res = defaultdict(list)

        for word in strs:
            chars  = [0]*26
            for char in word:
                chars[ord(char) - ord('a')] +=1

            immutable = tuple(chars)
            res[immutable].append(word)
        
        return list(res.values())
            
