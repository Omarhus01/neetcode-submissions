class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        start = 0 
        end = n - 1 
        
        while start <= end:
            #check if the current thing we are at is not alpha numeric, if  not, we continu, if yes 
            # we increment left adn we check it for ther end as well , and decrement 

            #check 1st if not alnum for  start , then we pass it and continue not doing anything yet 
            if  not s[start].isalnum():
                start+=1
                continue 
            # then we do it  again for the end one 
            elif not s[end].isalnum():
                end -= 1
                continue 
            # here is the actual comparision works 
            else:
                if s[start] != s[end]:
                    return False
            #be carefukl that the actual  incre,enmtr/decrementr happeend in the scope of the while loop 
            # not in the else , focus on the indentation or it can belong to the else block 
                start +=1 
                end  -= 1
        return True
        #time is O(n) since we need t check all chars and non chars to validate it 
        #space: O(n)this is a tricky one , casuse for the begining you will see that there is no 
        #extras space , but actually s.lower() made a neew array of having all of e elements in lowercase 
        #NOTE: Strings in python are immutable so this is why we have to create a new string modified 
        #



        