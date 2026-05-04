class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        the easiest way to work on this is by spitting  each workd to its chars and combine the  lieked ones 
         so we need o to have a key of chars gathered tgt and the values will be alist of all words 
         with these chars 
         sonce we are working n on alphabet , we need to creata an empty array os size 26 and count the 
         frequency of each char of each word , and we can do this 
         by getting the ascii result of subtracting the values and incrememntn it in the array we made 

         we are looking for a list of lists so we need a dummy place to have these lists, adn we add the values on
         only since these are the lists we are looking for 

        """

        from collections import defaultdict

        group = defaultdict(list)


        for word in strs:
            count = [0] * 26 # count here is just the array [0,0,0,0,0,0,0,....0]
            for ch in word:
                count[ord(ch) - ord('a')] +=1 #here the array is updated[1,0,0,1,0,0,0,,...1,0,0]
            group[tuple(count)].append(word)#tuplle here took the whole count array and returned 
            #it just as a tuple instead of a list, so it's immutable --> can be used as a key then.

        return list(group.values()) #we already built it so getting the value is easy 


